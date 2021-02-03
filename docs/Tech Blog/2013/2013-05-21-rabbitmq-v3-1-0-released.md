---
title: "rabbitMQ : v3.1.1 released"
date: "2013-05-21"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

_EDIT: okay, they just released v3.1.1 so here it goes on portage as well !_

## _highlights_

- _relax validation of x-match binding to headers exchange for compatibility with brokers < 3.1.0_
- _fix bug in ack handling for transactional channels that could cause queues to crash_
- _fix race condition in cluster autoheal that could lead to nodes failing to re-join the cluster_

_3.1.1 changelog is [here](http://www.rabbitmq.com/release-notes/README-3.1.1.txt)._

I've bumped the rabbitMQ message queuing server on portage. This new version comes with quite a nice bunch of bugfixes and features.

## highlights

- eager synchronisation of slaves by policy (manual & automatic)
- **cluster "autoheal" mode** to automatically choose nodes to restart when a partition has occurred
- cluster "pause minority" mode to prefer partition tolerance over availability
- improved statistics (including charts) in the management plugin
- quite a bunch of performance improvements
- some nice memory leaks fixes

Read the full [changelog](http://www.rabbitmq.com/release-notes/README-3.1.0.txt).
