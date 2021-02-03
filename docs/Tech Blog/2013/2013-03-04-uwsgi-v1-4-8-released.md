---
title: "uWSGI : v1.4.8 released & v2.0 sneak peek"
date: "2013-03-04"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "uwsgi"
---

Yet another bump for uWSGI as upstream is working hard on the 1.9 branch which will lead to the 2.0 LTS version. I guess it's time I take a few moments to give you some hints about what's coming for the v2.0 of uWSGI, be aware that this is some heavy stuff.

## future v2.0 highlights

- **new fully non-blocking API** which applies to all plugins, this will benefit the perl/PSGI plugin as well
- faster uwsgi/HTTP/FastCGI/SCGI native sockets thanks to better parsers
- splitted error logging from request logging for enhanced debugging
- more **offloading** improvements such as a new function to write files on disk and non-blocking workers for static files service
- better static files handling thanks to the new caching system
- totally rewritten web cache system allows you to have multiple caches per instance and tune them finely
- replaced the old clustering system with a new **Legion subsystem** providing resources management (yeah you wouldn't need stuff like pacemaker to handle your uWSGI cluster)
- advanced exception subsystem
- SPDY v3 support
- **SNI support**
- support for HTTP router keepalive, auto-chunking, auto-gzip and **transparent websockets**
- a SSL router will be available
- **websockets API** sponsored by 20Tab S.r.l. (a company working on HTML5 browsers game, thanks guys)
- programmable internal router
- and of course, the Mono/ASP.NET plugin I talked about in my previous post

See the full and detailed list [here](https://github.com/unbit/uwsgi-docs/blob/master/Changelog-1.9.rst)

## v1.4.8 highlights

- added support for ruby 2.0
- removed the mono/asp.net plugin (a new, working one, is in 1.9)
- backported the improved carbon plugin
- fixed a corner-case bug with the caching subsystem (Laurent Luce)
- fixed ipcsem on Linux
- backported --not-log-alarm (negative version of --log-alarm)
- backported add\_timer and add\_rb\_timer api functions for the perl/psgi plugin
- backported --for-glob, this is like --for but with glob expansion (Guido Berhoerster)
- avoid gateways crash on master shutdown
- backported https re-handshake management
- **improved gevent timeout management**
- uWSGI can now be installed as a ruby gem
- backported --http-socket-modifier1/2
