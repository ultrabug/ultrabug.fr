---
title: "Renaming and reshaping Scylla tables using scylla-migrator"
date: "2020-11-06"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "scylla"
  - "spark"
---

We have recently faced a problem where some of the first Scylla tables we created on our main production cluster were not in line any more with the evolved schemas that recent tables are using.

This typical engineering problem requires either to keep those legacy tables and data queries or to migrate it to the more optimal model with the bandwagon of applications to be modified to query the data the new way... That's something nobody likes doing but hey, we don't like legacy at Numberly so let's kill that one!

To overcome this challenge we used the **scylla-migrator** project and I thought it could be useful to share this experience.

## How and why our schema evolved

When [we first approached ID matching tables](https://www.ultrabug.fr/evaluating-scylladb-for-production-2-2/) we chose to answer two problems at the same time: query the most recent data and keep the history of the changes per source ID.

This means that those tables included a date as part of their **PRIMARY KEY** while the partition key was obviously the matching table ID we wanted to lookup from:

```
CREATE TABLE IF NOT EXISTS ids_by_partnerid(  
partnerid text,  
id text,  
date timestamp,  
PRIMARY KEY ((partnerid), date, id)  
)  
WITH CLUSTERING ORDER BY (date DESC)
```

Making a table with an ever changing date in the clustering key creates what we call a _**history table**_. In the schema above the uniqueness of a row is not only defined by a partner_id / id couple but also by its date!

Quick caveat: you have to be careful about the actual date timestamp resolution since you may not want to create a row for every second of the same partner_id / id couple (we use an hour resolution).

History tables are good for analytics and we also figured we could use them for batch and real time queries where we would be interested in the "**_most recent ids for the given partner_id_**" (sometimes flavored with a LIMIT):

```
SELECT id FROM ids_by_partnerid WHERE partner_id = "AXZAZLKDJ" ORDER BY date DESC;
```

As time passed, real time Kafka pipelines started to query these tables hard and were mostly interested in "**_all the ids known for the given partner_id_**".

A sort of DISTINCT(id) is out of the scope of our table! For this we need a table schema that represents a condensed view of the data. We call them **_compact tables_** and the only difference with the history table is that the date timestamp is simply not part of the PRIMARY KEY:

```
CREATE TABLE IF NOT EXISTS ids_by_partnerid(
partnerid text,
id text,
seen_date timestamp,
PRIMARY KEY ((partnerid), id)
)
```

To make that transition happen we thus wanted to:

- rename history tables with an **__history_** suffix so that they are clearly identified as such
- get a compacted version of the tables (by keeping their old name) while renaming the _date_ column name to _seen_date_
- do it as fast as possible since we will need to stop our feeding pipeline and most of our applications during the process...

**STOP: it's not possible to rename a table in CQL!**

[![](images/news-workload-cop.png)](https://www.ultrabug.fr/wordpress/wp-content/uploads/2020/11/news-workload-cop.png)

## Scylla-migrator to the rescue

We decided to abuse the **[scylla-migrator](https://github.com/scylladb/scylla-migrator)** to perform this perilous migration.

As it was originally designed to [help users migrate from Cassandra to Scylla](https://www.scylladb.com/2019/02/07/moving-from-cassandra-to-scylla-via-apache-spark-scylla-migrator/) by leveraging Spark it seemed like a good fit for the task since we happen to own Spark clusters powered by Hadoop YARN.

### Building scylla-migrator for Spark < 2.4

Recent scylla-migrator does not support older Spark versions. The trick is to look at the README.md git log and checkout the hopefully right commit that supports your Spark cluster version.

In our case for Spark 2.3 we used git commit bc82a57e4134452f19a11cd127bd4c6a25f75020.

On Gentoo, make sure to use **dev-java/sbt-bin** since the non binary version is vastly out of date and won't build the project. You need at least version 1.3.

### The scylla-migrator plan

The documentation explains that we need a config file that points to a source cluster+table and a destination cluster+table as long as they have the same schema structure...

Renaming is then as simple as duplicating the schema using CQLSH and running the migrator!

But what about our compacted version of our original table? The schema is different from the source table!...

**Good news is that as long as all your columns remain present, you can also change the PRIMARY KEY of your destination table and it will still work!**

This make the scylla-migrator an amazing tool to reshape or pivot tables!

- the column **date** is renamed to **seen_date**: that's okay, **scylla-migrator supports column renaming** (it's a Spark dataframe after all)!
- the PRIMARY KEY is different in the compacted table since **we removed the 'date**' from the clustering columns: we'll get a compacted table for free!

### Using scylla-migrator

The documentation is a bit poor on how to submit your application to a Hadoop YARN cluster but that's kind of expected.

It also did not mention how to connect to a SSL enabled cluster (are there people really not using SSL on the wire in their production environment?)... anyway let's not start a flame war :)

The trick that will save you is to know that you can append all the usual Spark options that are available in the [spark-cassandra-connector](https://github.com/datastax/spark-cassandra-connector/)!

Submitting to a **Kerberos protected Hadoop YARN cluster targeting a SSL enabled Scylla cluster** then looks like this:

```
export JAR_NAME=target/scala-2.11/scylla-migrator-assembly-0.0.1.jar
export KRB_PRINCIPAL=USERNAME

spark2-submit \
 --name ScyllaMigratorApplication \
 --class com.scylladb.migrator.Migrator  \
 --conf spark.cassandra.connection.ssl.clientAuth.enabled=True  \
 --conf spark.cassandra.connection.ssl.enabled=True  \
 --conf spark.cassandra.connection.ssl.trustStore.path=jssecacerts  \
 --conf spark.cassandra.connection.ssl.trustStore.password=JKS_PASSWORD  \
 --conf spark.cassandra.input.consistency.level=LOCAL_QUORUM \
 --conf spark.cassandra.output.consistency.level=LOCAL_QUORUM \
 --conf spark.scylla.config=config.yaml \
 --conf spark.yarn.executor.memoryOverhead=1g \
 --conf spark.blacklist.enabled=true  \
 --conf spark.blacklist.task.maxTaskAttemptsPerExecutor=1  \
 --conf spark.blacklist.task.maxTaskAttemptsPerNode=1  \
 --conf spark.blacklist.stage.maxFailedTasksPerExecutor=1  \
 --conf spark.blacklist.stage.maxFailedExecutorsPerNode=1  \
 --conf spark.executor.cores=16 \
 --deploy-mode client \
 --files jssecacerts \
 --jars ${JAR_NAME}  \
 --keytab ${KRB_PRINCIPAL}.keytab  \
 --master yarn \
 --principal ${KRB_PRINCIPAL}  \
 ${JAR_NAME}
```

**Note that we chose to apply a higher consistency level to our reads using a LOCAL_QUORUM instead of the default LOCAL_ONE.** I strongly encourage you to do the same since it's appropriate when you're using this kind of tool!

Column renaming is simply expressed in the configuration file like this:

```
# Column renaming configuration.
renames:
  - from: date
    to: seen_date
```

### Tuning scylla-migrator

While easy to use, **tuning scylla-migrator** to operate those migrations as fast as possible turned out to be a **real challenge** (remember we have some production applications shut down during the process).

Even using 300+ Spark executors I couldn't get my Scylla cluster utilization to more than 50% and migrating a single table with a bit more than 1B rows took almost 2 hours...

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fapprecs.org%2Fgp%2Fimages%2Fapp-icons%2F300%2Fc1%2Fspacevoyage.ru.unacceptable.jpg&f=1&nofb=1)

We found the best knobs to play with thanks to the help of Lubos Kosco and [this blog post from ScyllaDB](https://www.scylladb.com/2019/02/07/moving-from-cassandra-to-scylla-via-apache-spark-scylla-migrator/):

- Increase the **splitCount** setting: more splits means more Spark executors will be spawned and more tasks out of it. While it might be magic on a pure Spark deployment it's not that amazing on a Hadoop YARN one where executors are scheduled in containers with 1 core by default. We simply moved it from 256 to 384.
- **Disable compaction on destination tables schemas**. This gave us a big boost and saved the day since it avoids adding the overhead of compacting while you're pushing down data hard!

To disable compaction on a table simply:

```
ALTER TABLE ids_by_partnerid_history WITH compaction = {'class': 'NullCompactionStrategy'};
```

**Remember to run a manual compaction** using `nodetool compact <keyspace> <table>` and to **enable compaction back on your tables once you're done!**

Happy Scylla tables mangling!
