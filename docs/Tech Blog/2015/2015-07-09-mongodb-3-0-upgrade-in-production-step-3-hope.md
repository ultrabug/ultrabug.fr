---
title: "MongoDB 3.0 upgrade in production : step 3 hope"
date: "2015-07-09"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
---

[In our previous attempt](http://www.ultrabug.fr/mongodb-3-0-upgrade-in-production-step-2-failed/) to upgrade our production cluster to 3.0, we had to roll back from the WiredTiger engine on primary servers.

Since then, we switched back our whole cluster to **3.0 MMAPv1** which has brought us **some better performances than 2.6** with no instability.

## Production checklist

We decided to use this increase in performance to allow us some time to fulfil the entire [production checklist](http://docs.mongodb.org/manual/administration/production-checklist/) from MongoDB, **especially the migration to XFS**. We're slowly upgrading our servers kernels and resynchronising our data set after migrating from ext4 to XFS.

Ironically, the strong recommendation of XFS in the production checklist [appeared 3 days after](https://github.com/mongodb/docs/commit/53e6178f8085de8ba997bc8a54d46bad25fc04c4) our failed attempt at WiredTiger... This is frustrating but gives some kind of hope.

I'll keep on posting on our next steps and results.

## Our hero WiredTiger Replica Set

While we were battling with our production cluster, we got a spontaneous major increase in the daily volumes from another platform which was running on a single Replica Set. This application is write intensive and very disk I/O bound. We were killing the disk I/O with almost a continuous 100% usage on the disk write queue.

Despite our frustration with WiredTiger so far, we decided to give it a chance considering that this time we were talking about a single Replica Set. We were very happy to see **WiredTiger keep up to its promises with an almost shocking serenity**.

Disk I/O went down dramatically, almost as if nothing was happening any more. Compression did magic on our disk usage and our application went **Roarrr** !
