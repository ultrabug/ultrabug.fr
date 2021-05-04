---
title: "uWSGI : v1.2.6 and v1.3 released"
date: "2012-10-29"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "release"
  - "uwsgi"
---

The v1.2.6 is a maintenance release with some interesting backports while the v1.3 series start with a couple of new interesting features and plugins such as a mongodb logger. On my async python usage side, I'm glad to see this new version coming for its enhanced [\--lazy-apps](http://projects.unbit.it/uwsgi/wiki/ThingsToKnow) option and gevent grace reloading.

## v1.2.6 highlights :

- fixed idle mode on busy workers
- backported subscription round robin weight handling from 1.3

See the complete [changelog](http://lists.unbit.it/pipermail/uwsgi/2012-September/004679.html).

## v1.3 highlights :

- New plugin : router_http (compiled-in by default)
- New feature : --if-env (and --if-opt) can compare values
- http/https non-blocking writes
- Busyness cheaper algorithm by Łukasz Mierzwa
- MongoDB integration for logging
