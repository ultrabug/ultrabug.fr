---
title: "Clustering : corosync v2.3.0 & resource-agents-3.9.4"
date: "2013-01-18"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "corosync"
  - "gentoo"
  - "portage"
  - "release"
---

Some new stuff related to clustering are now available on portage ! Here are the highlights.

## crmsh-1.2.4

- better pacemaker-1.1.8 compatibility
- fine tuning history and regression fixes

## resource-agents-3.9.4

Oh yes I've been slacking on that one but it's finally here ! As a reminder this huge bump (1.0.4 -> 3.9.4) is the result of the upstream merge from the pacemaker and rgmanager resource agents developments. This is reflected by a new _rgmanager_ USE flag for those who want to install those resources.

- **zabbixserver** : new resource agent
- **IPaddr2**: partial rewrite and support for IPv6
- **iscsi**: support for auto recovery and performance improvements
- tools: replace the findif binary by findif.sh

See the full [changelog](https://github.com/ClusterLabs/resource-agents/blob/master/ChangeLog).

## corosync-1.4.5 and corosync-2.3.0

The next releases of the flatiron and needle branches of corosync are rich of bug fixes, man updated and performance improvements. I wasn't able to find the proper changelog pages but you can have a look [here](http://www.spinics.net/lists/corosync/msg02286.html) where a bunch of the fixes are listed.
