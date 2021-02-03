---
title: "Scylla: four ways to optimize your disk space consumption"
date: "2019-03-29"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "optimization"
  - "scylla"
---

We recently had to face free disk space outages on some of our scylla clusters and we learnt some very interesting things while outlining some improvements that could be made to the ScyllaDB guys.

![](images/2019-03-29-120403_219x158_scrot.png)

### 100% disk space usage?

First of all I wanted to give a bit of a heads up about what happened when some of our scylla nodes reached (almost) 100% disk space usage.

Basically they:

- stopped listening to client requests
- complained in the logs
- wouldn't flush commitlog (expected)
- abort their compaction work (which actually gave back a few GB of space)
- stay in a stuck / unable to stop state (unexpected, this has been reported)

After restarting your scylla server, the first and obvious thing you can try to do to get out of this situation is to run the **nodetool clearsnapshot** command which will remove any data snapshot that could be lying around. That's a handy command to reclaim space usually.

_Reminder: depending on your compaction strategy, it is usually not advised to allow your data to grow over 50% of disk space._..

But that's only a patch so let's go down the rabbit hole and look at the optimization options we have.

* * *

### Optimize your schemas

Schema design and the types your choose for your columns have a huge impact on disk space usage! And in our case we indeed overlooked some of the optimizations that we could have done from the start and that did cost us a lot of wasted disk space. Fortunately it was easy and fast to change.

To illustrate this, I'll take a sample of 100,000 rows of a simple and naive schema associating readings of 50 integers to a user ID:

_Note: all those operations were done using Scylla 3.0.3 on Gentoo Linux._

CREATE TABLE IF NOT EXISTS test.not\_optimized  
(  
    uid text,  
    readings list<int>,  
    PRIMARY KEY(uid)  
) WITH compression = {};

Once inserted on disk, this takes about **250MB** of disk space:

250M    not\_optimized-00cf1500520b11e9ae38000000000004

Now depending on your use case, if those readings at not meant to be updated for example you could use a **frozen list** instead, which will allow a huge storage optimization:

CREATE TABLE IF NOT EXISTS test.mid\_optimized  
 (  
     uid text,  
     readings frozen<list<int>>,  
     PRIMARY KEY(uid)  
 ) WITH compression = {};

With this frozen list we now consume **54MB** of disk space **for the same data**!

54M     mid\_optimized-011bae60520b11e9ae38000000000004

There's another optimization that we could do since our user ID are UUIDs. Let's switch to the **uuid type instead of text**:

CREATE TABLE IF NOT EXISTS test.optimized  
 (  
     uid uuid,  
     readings frozen<list<int>>,  
     PRIMARY KEY(uid)  
 ) WITH compression = {};

By switching to **uuid**, we now consume **50MB** of disk space: that's a **80% reduced disk space consumption** compared to the naive schema for the same data!

50M     optimized-01f74150520b11e9ae38000000000004

### Enable compression

All those examples were not using compression. If your workload latencies allows it, you should probably enable compression on your sstables.

Let's see its impact on our tables:

ALTER TABLE test.not\_optimized WITH compression = {'sstable\_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'};  
ALTER TABLE test.mid\_optimized WITH compression = {'sstable\_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'};  
ALTER TABLE test.optimized WITH compression = {'sstable\_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'};

Then we run a **nodetool compact test** to force a (re)compaction of all the sstables and we get:

63M     not\_optimized-00cf1500520b11e9ae38000000000004  
28M     mid\_optimized-011bae60520b11e9ae38000000000004  
24M     optimized-01f74150520b11e9ae38000000000004

Compression is really a great gain here allowing another **50% reduced disk space usage reduction on our optimized table**!

### Switch to the new "mc" sstable format

Since the Scylla 3.0 release you can use the latest "mc" sstable storage format on your scylla clusters. It promises a greater efficiency for [usually a way more reduced disk space](https://www.scylladb.com/2019/01/24/scylla-sstable-3-0-can-decrease-file-sizes-50-or-more/) consumption!

It is **not** enabled by default, you have to add the **enable\_sstables\_mc\_format: true** parameter to your scylla.yaml for it to be taken into account.

Since it's backward compatible, you have nothing else to do as new compactions will start being made using the "mc" storage format and the scylla server will seamlessly read from old sstables as well.

But in our case of immediate disk space outage, we switched to the new format one node at a time, dropped the data from it and ran a **nodetool rebuild** to reconstruct the whole node using the new sstable format.

Let's demonstrate its impact on our test tables: we add the option to the **scylla.yaml** file, restart scylla-server and run n**odetool compact test** again:

49M     not\_optimized-00cf1500520b11e9ae38000000000004  
26M     mid\_optimized-011bae60520b11e9ae38000000000004  
22M     optimized-01f74150520b11e9ae38000000000004

That's a pretty cool gain of disk space, even more for the not optimized version of our schema!

So if you're in great need of disk space or it is hard for you to change your schemas, switching to the new "mc" sstable format is a simple and efficient way to free up some space without effort.

### Consider using secondary indexes

While denormalization is the norm (_yep.. legitimate pun_) in the NoSQL world this does not mean we have to duplicate everything all the time. A good example lies in the internals of **secondary indexes** if your workload can compromise with its moderate impact on latency.

Secondary indexes on scylla are built on top of Materialized Views that basically stores an up to date pointer from your indexed column to your main table partition key. That means that **secondary indexes MVs are not duplicating all the columns (and thus the data) from your main table** as you would have to do when denormalizing a table to query by another column: **this saves disk space!**

This of course comes with a latency drawback because if your workload is interested in the other columns than the partition key of the main table, the coordinator node will actually issue two queries to get all your data:

1. query the secondary index MV to get the pointer to the partition key of the main table
2. query the main table with the partition key to get the rest of the columns you asked for

This has been an effective trick to avoid duplicating a table and save disk space for some of our workloads!

### (not a tip) Move the commitlog to another disk / partition?

This should only be considered as a sort of emergency procedure or for cost efficiency (cheap disk tiering) on **non critical clusters**.

While this is possible even if the disk is not formatted using XFS, it not advised to separate the commitlog from data on modern SSD/NVMe disks but... you technically can do it (as we did) **on non production clusters**.

Switching is simple, you just need to change the **commitlog\_directory** parameter in your scylla.yaml file.
