---
title: "mongoDB v2.4.9/v2.2.7, rabbitMQ v3.2.3"
date: "2014-02-18"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "rabbitmq"
  - "releases"
---

Quick post about some recent bumps.

## mongodb-2.4.9 & mongodb-2.2.7

**IMPORTANT** : These versions fix a mongos [bug](https://jira.mongodb.org/browse/SERVER-12146) which could lead it to report a write as successful when it was not. This affects all versions of MongoDB prior to and including v2.4.8.

- v2.4.9 [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/13116)
- v2.2.7 [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/12902)

Stay tuned on mongoDB, the next post will probably talk about the release of **pymongo v2.7** which supports some neat futures from the upcoming mongoDB v2.6 series.

## rabbitMQ-3.2.3

I skipped a bump post when releasing the [v3.2.2](http://www.rabbitmq.com/release-notes/README-3.2.2.txt) so you should check out the [v3.2.3](http://www.rabbitmq.com/release-notes/README-3.2.3.txt) changelog as well if you're willing to know more about those bug fix releases.
