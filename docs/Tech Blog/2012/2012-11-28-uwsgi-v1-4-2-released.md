---
title: "uWSGI : v1.4.2 released"
date: "2012-11-28"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

Quick post for a bugfix release with some added flavor features for PHP users.

## highlights

- improved perl mules support
- fixed pending datas management in https router
- fixed thread-offloading of really big static files
- added --php-app-qs as micro-optimization (in-place of rewrite rules) for php apps
- added --php-var to inject custom (fixed) vars in the request

Full [changelog here](http://lists.unbit.it/pipermail/uwsgi/2012-November/005111.html), as usual.
