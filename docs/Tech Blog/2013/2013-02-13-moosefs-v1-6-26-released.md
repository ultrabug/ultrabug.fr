---
title: "MooseFS : v1.6.26 released"
date: "2013-02-13"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "moosefs"
  - "portage"
  - "release"
---

This was one of my first package creation in portage and although it doesn't have a quick iteration I still find this software very interesting. I was glad to see upstream release a new stable version but I have to admit I slacked quite a lot on actually seeing this bump (2012-08-16) :) Anyway, it's now live for some time in portage and I hope some folks were happy to update their platform with it.

## changelog

- (all) fixed signal handling in multithreaded modules
- (master) added goal and trashtime limits to mfsexport.cfg
- (metalogger) added simple check for downloaded metadata file (inspired by Davies Liu)
- (master) better handle disk full (inspired by Davies Liu)
- (master+metalogger) added keeping previous copies of metadata (inspired by Davies Liu)
- (all) reload all settings on "reload" (SIGHUP)
- (cs) disk scanning in background
- (cs) fixed long termination issue (found by Davies Liu)
