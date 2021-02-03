---
title: "rabbitMQ : v3.1.4 released"
date: "2013-08-13"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

Quick post for a quick bugfix release of the rabbitMQ server. Please note that I dropped the remaining 3.0.4 version in tree while doing this bump.

## highlights

- **security fix** : ensure DLX declaration checks for publish permission (since 2.8.0)
- **security fix** : update to a later version of Mochiweb that fixes a directory traversal vulnerability allowing arbitrary file access on Windows (since 2.1.0)
- fix resource leak with mirrored queues when whole clusters stop (since 3.0.0)
- fix queue crash in mirrored queue handling of messages during promotion (since 2.6.0)
- fix mirrored queue sync failure in the presence of un-acked messages not at the head of the queue (since 3.1.0)
- allow hipe compilation on Erlang R16B01
- make \`rabbitmqctl join\_cluster' idempotent (since 3.0.0)
- improve \`rabbitmqctl cluster\_status' handling of partition info when cluster nodes are in the process of stopping (since 3.1.0)
