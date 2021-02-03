---
title: "mongoDB v2.4.2 released"
date: "2013-04-18"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "release"
---

After the security issue related bumps of the previous releases which happened last weeks it was about time 10gen released a 2.4.x fixing the following issues:

- Fix for upgrading sharded clusters
- TTL assertion on replica set secondaries
- Several V8 memory leak and performance fixes
- High volume connection crash

I guess everything listed above would have affected our cluster at work so I'm glad we've been patient on following-up this release :) See the [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/12405) for details.
