---
title: "uWSGI : v1.4.9 released"
date: "2013-03-11"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

Yet another version bump for this very active package.

## highlights

- avoid crashing carbon on master shutdown
- call ERR_clear_error after each https session close
- fixed broodlord mode
- removed broken JVM and JWSGI plugins (stable versions are in 1.9)
- backported cache_update for lua and fixed its lock handling

Full [changelog](http://lists.unbit.it/pipermail/uwsgi/2013-March/005591.html) is here.
