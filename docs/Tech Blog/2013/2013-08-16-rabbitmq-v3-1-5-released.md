---
title: "rabbitMQ : v3.1.5 released"
date: "2013-08-16"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

Looks like rabbitMQ upstream likes to bump their stuff right after I catch-up with my bumps :) **You are strongly advised to upgrade to this version since it fixes a quite important bug introduced by 3.1.4.**

## highlights

- fix crash in the delegate mechanism leading to various crashes, and intra-cluster incompatibility between RabbitMQ 3.1.4 and other members of the 3.1.x series (since 3.1.4)
- prevent (harmless) errors being logged when pausing in pause_minority mode (since 3.1.0)
