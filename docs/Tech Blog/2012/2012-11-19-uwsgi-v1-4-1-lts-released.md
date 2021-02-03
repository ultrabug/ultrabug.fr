---
title: "uWSGI : v1.4.1 LTS released"
date: "2012-11-19"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "release"
  - "uwsgi"
---

Ok that's a neat uwsgi release here and stamped for Long Time Support by unbit. I've tested it before bumping it to portage and it's behaving nicely with my gevent apps as there have been some nice improvements on this part as well. Quite a bunch of code have been refactored and optimized for enhanced performances. Have a look at the highlights, they're to be read with care.

## highlights :

- Support for the **Go** language
- Enhanced **gevent** reloading and handling (truly non-blocking wsgi.input, truly non-blocking writes...)
- Improved http/https router and **fastrouter** (better event-based engineering, reduced syscall usage)
- Improved **systemd** support
- Log filtering and routing
- [Smart attach daemon](http://uwsgi-docs.readthedocs.org/en/latest/AttachingDaemons.html) to start a daemon along with your app
- A big work is being done about the [documentation](http://uwsgi-docs.readthedocs.org/en/latest/index.html)

Yep that's some heavy stuff, there is more so you should definitely read the different changelogs on the [mailing list](http://lists.unbit.it/pipermail/uwsgi/2012-November/thread.html) !
