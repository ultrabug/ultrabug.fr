---
title: "uWSGI : v1.2.4 released"
date: "2012-07-09"
categories: 
  - "linux"
tags: 
  - "ebuild"
  - "gentoo"
  - "release"
  - "uwsgi"
---

This is a maintenance release of uWSGI whicih contains two new features and lot of bug fixes, it is now available in portage. Two of those fixes I was longing for :)

## Bug fix highlights :

- fixed python atexit usage in the spooler
- fixed a threading issue with uwsgi.send()
- fixed a leak in python uwsgi.workers()
- fixed spooler with chdir
- fixed async+threading
- **fixed the spooler-max-tasks respawn**
- **allow gevent's greenlets to send jobs to the spooler**

See the complete [changelog](http://lists.unbit.it/pipermail/uwsgi/2012-July/004460.html).
