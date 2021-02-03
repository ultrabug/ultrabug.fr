---
title: "uWSGI : v1.4.3 released"
date: "2012-12-13"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

Bugfix release with a few features.

## highlights

- close useless file descriptors when spawning daemons or external commands
- fixed log format in cheaper busyness algo
- allow to override the number of cpus detected by the build system using the CPUCOUNT env var

See the full [changelog](http://lists.unbit.it/pipermail/uwsgi/2012-December/005165.html).
