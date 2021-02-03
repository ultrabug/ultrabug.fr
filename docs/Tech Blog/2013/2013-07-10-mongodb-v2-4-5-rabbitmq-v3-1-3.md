---
title: "mongoDB v2.4.5 & rabbitMQ v3.1.3"
date: "2013-07-10"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "portage"
  - "rabbitmq"
  - "release"
---

Quick catch-up on _recent_ bumps I've made for **rabbitMQ** and **mongoDB** before posting about EuroPython2013 !

## mongoDB v2.4.5

The 2.4 branch is definitely the most bugged one I've seen so far. We waited until 2.4.4 at work before migrating but this was not enough and we got hit for a few weeks by a bug which finally got fixed in 2.4.5. Also this release fixes [two security bugs](https://bugs.gentoo.org/show_bug.cgi?id=475750) so you're strongly advised to upgrade.

### highlights

- CVE-2013-4650 - Improperly grant user system privileges on databases other than “local”.
- CVE-2013-4650 - Remotely triggered segmentation fault in Javascript engine.
- config server performance improvements
- improve initial sync resilience to network failure (that's the one)

### flask-pymongo v0.3.0

@dcrosta finally had the time to take care of my pull request for **flask-pymongo**. We now rely on pymongo's MongoClient parameters' validation instead of implementing them again on flask-pymongo and added connect and socket timeout options.

## rabbitMQ v3.1.3

A roll-up bugfix release mainly.

### highlights

- fix startup failure when using SSL with Erlang/OTP R16B01
- fix queue crash requeuing in-memory messages (since 2.7.0)
- fix leak affecting HA/mirrored queues (since 3.0.0)
- fix bug that lead to incorrect reporting of accumulated stats (since 3.1.2)
