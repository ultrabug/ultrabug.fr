---
title: "uWSGI : v1.2.5 released"
date: "2012-08-14"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "release"
  - "uwsgi"
---

This is a maintenance release of uWSGI with one new feature supporting pam authentication mechanism. The ebuild has been bumped with a new _pam_ USE flag.

## Bug fix highlights :

- allows ugreen with threads
- added the pam plugin (sponsored by PythonAnywhere.com)
- added --so-keepalive option to enable TCP keepalives on sockets

See the complete [changelog](http://lists.unbit.it/pipermail/uwsgi/2012-August/004597.html).
