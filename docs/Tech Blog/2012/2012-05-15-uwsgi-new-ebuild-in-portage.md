---
title: "uWSGI : new ebuild in portage"
date: "2012-05-15"
categories: 
  - "linux"
tags: 
  - "ebuild"
  - "portage"
  - "uwsgi"
---

I started to rework the **uwsgi ebuild** on March 7th because I was not satisfied with the one available in portage. The current version was out of date and the package itself was not really suited for production deployment.

Luckily my fellow Gentoo Linux developer Tiziano Müller (dev-zero) was also in the same kind of process for his own needs so we teamed up to achieve this goal. Our main focuses were :

- Bring the emperor mode support
- Ease and clarify the overall configuration
- Code a more versatile init script and conf.d file
- Add a better support of the available plugins and python versions
- Support PHP

I'm glad to announce that our reworked ebuild is now available in portage for all users, we hope that it will come handy to everyone who needs it.

Thanks again Tiziano, it's always a pleasure to work with you !
