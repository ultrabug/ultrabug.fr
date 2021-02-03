---
title: "uWSGI : v1.4.6 released"
date: "2013-02-26"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

This is quite a big release for its backports and improvements. But there are two more interesting things to note here : uWSGI supports Heroku and Dreamhost deployments !

## tutorials

- [uWSGI + Heroku + Python tutorial](https://github.com/unbit/uwsgi-docs/blob/master/tutorials/heroku_python.rst)
- [uWSGI + Dreamhost tutorial](https://github.com/unbit/uwsgi-docs/blob/master/tutorials/dreamhost.rst)

## highlights

- fix SERVER\_PORT value in corerouters when using shared sockets
- backported --thunder-lock option to reduce thundering herd problem (use with caution)
- fixed **pthread robust mutexes in newer glibc**
- backported improvements for the alarm\_xmpp plugin
- fixed suspend when harakiri is in place
- reset sigmask on startup
- **fixed master+emperor configurations**
- backported more logvars (check here: https://uwsgi-docs.readthedocs.org/en/latest/LogFormat.html)
- **fixed muleloop in uwsgidecorators**
- fixed a refcnt bug in the psgi plugin spotted by Nick Gregory (issue #158)
- backported **new python build system** (Heroku friendly)
- backported --perl-arg and --perl-args options (to add items in @ARGV)
- backported perl async fixes
- allows --attach-daemon without workers
