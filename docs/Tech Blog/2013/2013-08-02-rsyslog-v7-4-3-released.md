---
title: "rsyslog : v7.4.3 released"
date: "2013-08-02"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "rsyslog"
---

It's been more than 3 months since the last version bump of rsyslog, I'm sorry about that (special kudos to @Opportunist for his patience). Since June 6th, we have a new stable 7.4 branch of rsyslog containing all the bugfixes and improvements made in the 7.3 dev branch.

So here comes the catch-up to current v7.4.3. **Please note that as upstream do not support older branches, I will soon remove them from portage and close related bugs.**

## highlights

- tons of bugfixes I won't bother to list
- imjournal: add ratelimiting capability
- max number of templates for plugin use has been increased to five
- added support for encrypting log files
- omhiredis: added support for redis pipeline support
