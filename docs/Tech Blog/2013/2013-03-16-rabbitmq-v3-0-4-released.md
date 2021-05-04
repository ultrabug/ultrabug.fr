---
title: "rabbitMQ : v3.0.4 released"
date: "2013-03-16"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

Within a week, rabbitMQ got bumped twice. I'm happy to quickly post about those recent bumps so here is a highlight of [3.0.3](http://www.rabbitmq.com/release-notes/README-3.0.3.txt) and [3.0.4](http://www.rabbitmq.com/release-notes/README-3.0.4.txt) changelogs.

## highlights

- fix connection failure to start reading again in rare circumstances when coming out of flow control
- ensure invocation of "rabbitmqctl stop_app" during server startup on a fresh node does not leave a corrupted Mnesia schema
- ensure messages expire immediately when reaching the head of a queue after basic.get
- ensure parameters and policies for a vhost are removed with that vhost
- do not log spurious errors for connections that close very early
- ensure "rabbitmqctl forget_cluster_node" removes durable queue records for unmirrored queues on the forgotten node
- clean up connection and channel records from nodes that have crashed
- do not show 404 errors when rabbitmq_federation_management is installed and rabbitmq_federation is not
- ensure the reader process hibernates when idle
- prevent x-received-from header from leaking upstream credentials
