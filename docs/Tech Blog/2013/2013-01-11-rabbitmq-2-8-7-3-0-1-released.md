---
title: "rabbitMQ 2.8.7 & 3.0.1 released"
date: "2013-01-11"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

It took me quite a while to bump this package as v3.0.0 and v3.0.1 were released respectively on Nov. 19 and Dec. 11 but here they are. This bump is dedicated to Jasper @darkroom bar in NZ :)

Anyway, that's quite a huge release for the rabbitMQ team which they described themselves very well :

This release introduces dynamic, policy-based control of mirroring and federation, improves the user friendliness of clustering, adds support for per-message TTL, introduces plugins for web-STOMP and MQTT, and adds many smaller new features and bug fixes.

In addition, performance is improved in several cases. Most notably, mirrored queues are substantially faster.

So my highlights will be very modest compared to the real thing and I strongly encourage you to spend 5 minutes to read the changelogs.

## highlights

- allow queue mirroring to be defined by broker-wide policy, not queue declaration, and add "exactly" mode
- support per-message TTL
- enable heartbeats by default
- remove support for AMQP's "immediate" publish mode
- greatly improve performance of mirrored queues
- improve performance of SSL when using HiPE compilation
- improve performance of bulk dead-lettering
- new plugin: implement Message Queue Telemetry Transport version 3.1
- allow mixed patch versions of RabbitMQ in a cluster

 

Read the [3.0.0 changelog](http://www.rabbitmq.com/release-notes/README-3.0.0.txt) and [3.0.1 changelog](http://www.rabbitmq.com/release-notes/README-3.0.1.txt) for more juicy stuff.
