---
title: "mongoDB v2.4.8, rabbitMQ v3.2.1, rsyslog v7.4.6"
date: "2013-11-09"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "rabbitmq"
  - "release"
---

## mongodb-2.4.8

You should consider this **important** update if you have a **cluster** **running** **v2.4.7**. It contains a fix for the config servers which can have them possibly disagree on chunks hashes and thus prevent mongos to start or balancing to happen. See [this bug](https://jira.mongodb.org/browse/SERVER-11421) for more info.

## rabbitMQ-3.2.1

The famous message queuing server got a nice bunch of bug fixes on a lot of its modules along with some interesting additions such as :

- support for federated queues
- report client authentication errors during connection establishment explicitly using connection.close
- inform clients when memory or disk alarms are set or cleared
- allow policies to target queues or exchanges or both
- offer greater control over threshold at which messages are paged to disk
- allow missing exchanges & queues to be deleted and unbound without generating an AMQP error
- implement consumer priorities

Full changelog [here](http://www.rabbitmq.com/release-notes/README-3.2.0.txt) and [here](http://www.rabbitmq.com/release-notes/README-3.2.1.txt).

## rsyslog-7.4.6

This is a bug fix release, nothing too big about it as [reported](https://bugs.gentoo.org/show_bug.cgi?id=490469) by Thomas D (thanks again).

Please note that **rsyslog-7.4.4 is being stabilized**, mainly for [security purposes](https://bugs.gentoo.org/show_bug.cgi?id=475882).
