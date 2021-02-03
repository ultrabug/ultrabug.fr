---
title: "mongoDB : v2.0.6 released"
date: "2012-06-06"
categories: 
  - "linux"
tags: 
  - "logrotate"
  - "mongodb"
  - "nosql"
  - "release"
---

Bug fix release, it is now available in portage. Starting from this package version I introduced a **logrotate** script which compresses daily the mongodb logs and keeps them for a year.

Release **highlights** :

- mongos does not send reads to secondaries after replica restart when using keyFiles
- If only slaveDelay'd nodes are available, use them
- OplogReader has no socket timeout

See the the complete [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/11165).
