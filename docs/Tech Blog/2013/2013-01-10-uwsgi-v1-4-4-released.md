---
title: "uWSGI : v1.4.4 released"
date: "2013-01-10"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

Bug fix release only, I've just bumped it on portage.

## highlights

- backported a couple of fixes for the https router
- fixed wrong typecasting in yaml and fixed subscription system on 32 bit
- added and additional error report for the gevent plugin if a read() fails
- improved apache2 mod\_proxy\_uwsgi

See the full [changelog](http://lists.unbit.it/pipermail/uwsgi/2012-December/005184.html) as usual.
