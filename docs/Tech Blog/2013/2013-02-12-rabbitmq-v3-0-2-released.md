---
title: "rabbitMQ : v3.0.2 released"
date: "2013-02-12"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

Quick post for a bugfix release.

## highlights

- fix broken error reporting for rabbitmqctl
- fix race causing queues to crash when stopping mirroring
- prevent rabbitmqctl status from killing web-STOMP connections
- fix hang of rabbitmqctl status when JSON-RPC plugin enabled

Read the full [changelog](http://www.rabbitmq.com/release-notes/README-3.0.2.txt).
