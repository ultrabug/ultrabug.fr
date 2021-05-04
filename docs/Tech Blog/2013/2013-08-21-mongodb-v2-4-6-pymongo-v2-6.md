---
title: "mongoDB v2.4.6 & pymongo v2.6"
date: "2013-08-21"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "pymongo"
  - "release"
---

## mongodb-2.4.6

The folks at 10gen discovered a **severe bug** in the mongoDB chunk migration process on sharded environments.

Basically, depending of the size of your documents, there was a chance **that some get lost during data migration** ! Relax tho, this case affected only the chunks containing documents which size are in the range of 16,776,185 and 16,777,216 bytes (inclusive) so this means that if you don't have quite big documents in your cluster, you have not been affected by this bug.

Still, as a maintainer and production user of mongoDB, this is not the kind of news I like to hear especially when thinking of you Gentoo users. On top of this, I had the bad surprise to experience again the stale replication bug that was supposed to be fixed on 2.4.5 on my production cluster.

So I decided this was time for a major cleanup of the mongoDB ebuilds in portage to make sure we're not shipping known broken versions of mongoDB to you guys. I thus :

- dropped all obsolete <mongodb-2.2 ebuilds (I warned about this quite some time ago now)
- dropped the known bugged versions of mongodb (<2.2.6 and <2.4.6)
- cleaned up all obsolete files in $FILESDIR
- added, on the v2.4.6 ebuild, the **embedded-v8** USE flag **as a user convenience** so you can now have packages requiring v8-3.19 and mongodb installed on your machine. I added an explicit warning about this as **this is not the way to go** on normal usage as this is against Gentoo policy.

\*mongodb-2.4.6 (21 Aug 2013)
\*mongodb-2.2.6 (21 Aug 2013)

  21 Aug 2013; Ultrabug <ultrabug@gentoo.org> -mongodb-2.0.7-r1.ebuild,
  -mongodb-2.0.7-r2.ebuild, -mongodb-2.0.8-r1.ebuild, -mongodb-2.0.8-r2.ebuild,
  -mongodb-2.2.0-r1.ebuild, -mongodb-2.2.0-r2.ebuild, -mongodb-2.2.4.ebuild,
  +mongodb-2.2.6.ebuild, -mongodb-2.4.5.ebuild, -mongodb-2.4.6_rc1.ebuild,
  +mongodb-2.4.6.ebuild, -files/mongodb-1.8.5-fix-smokepy.patch,
  -files/mongodb-1.8-fix-scons.patch, -files/mongodb-2.2-fix-scons.patch,
  -files/mongodb-2.2-fix-sconscript.patch,
  -files/mongodb-2.4.4-fix-sharedclient.patch, -files/mongodb.initd,
  -files/mongodb-linux3.patch, -files/mongos.initd, metadata.xml:
  version bump, add embedded-v8 USE, drop critically bugged versions, drop
  obsolete versions, filesdir cleanup

I understand some people may still need some of those ebuilds so if that's the case, just shout and I'll gladly add them to my overlay so you can still use them easily.

### other highlights

- Improved replication robustness in presence of high network latency
- Resolved replica set initial sync issue on certain virtualized platforms
- Resolved sharding migration issue that produced excessive small chunks
- Resolved C++ client shutdown issues

## pymongo-2.6

This one is quite interesting as it brings both new and improved features as well as some bug fixes. Also note that they fixed some gevent compatibility stuff.

### highlights / explanations

- The **max_pool_size** option actually means what it says now. Pymongo will open at most this number of sockets to your servers. Do remember that if you share a connection between threads, then your (**max_pool_size**+1) thread will wait for a socket to be freed before being able to process your command.
- waitQueueMultiple and waitQueueTimeoutMS options will help you define how much and how long you want a process to wait for a socket to be available before raising an exception.
- Pymongo automatically splits batch inserts into 48MB chunks so you don't have to worry about pushing a huge list of documents for insertion.
- Support for aggregation cursors (for use with dev version 2.5.1, not used on production now)
- Support for **exhaust cursors.** When you queried a large amount of data, the client had to ask the server for each batch of results. An exhaust cursor will instead stream batches to the client as quick as possible. This make pulling large sets of data faster and more reliable than before !

You can see the full extend of this bump on the [pymongo Jira](https://jira.mongodb.org/secure/IssueNavigator.jspa?requestId=13849).
