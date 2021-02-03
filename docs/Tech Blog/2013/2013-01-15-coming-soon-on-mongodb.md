---
title: "Coming soon on mongoDB"
date: "2013-01-15"
categories: 
  - "linux"
tags: 
  - "mongodb"
  - "nosql"
---

Some interesting stuff is cooking on the 2.3.x development branch of mongoDB, let's take a look at what we can expect to see in the future 2.4.x releases.

## Switch to v8 Javascript engine

It's finally real since 2.3.1 as the folks at 10gen switched to v8 as the default JS engine powering mongoDB. This is a huge and a long time craved move which will primary **improve performance** and allow **concurrent queries** to be executed (aka collection level locking).

## Full text search

This one is around since 2.3.2 and will be available as a **new type of index** you'll have to create using the **textSearchEnabled=true** parameter. It's still a new feature under development so don't expect something able to compete with solr of course but still, it's a very nice feature ! You'll find more information about this on [A. Jesse Jiryu Davis' blog](http://emptysquare.net/blog/mongodb-full-text-search/).

## Other highlights

- **Aggregation framework performance** improvements
- New circular geospatial index type. Support for line, polygon, and point intersection queries as well as GeoJSON parsing.
- Better server stats framework
- Storage engine improvements to **reduce fragmentation**
- New operators : $push to sorted and fixed size arrays, $setOnInsert modifier for upserts, $geoNear and $within operators in aggregation framework
- **\_secondaryThrottle is now on by default** : this adds a write concern support for chunk migration reducing the replication lag caused by chunk moves
- **\--objcheck is now on by default** : the server validates the requests' objects before inserting the data. This used to have a slight performance impact but should be countered by v8 fairly well
