---
title: "rsyslog : v6.2.2 released"
date: "2012-06-15"
categories: 
  - "linux"
tags: 
  - "release"
  - "rsyslog"
---

This is a bug fix release of rsyslog, it is now [available in portage](https://bugs.gentoo.org/show_bug.cgi?id=420999).

# Bug fix highlights :

- disk queue was not persisted on shutdown
- \--enable-smcustbindcdr configure directive did not work (my fix, yay!)
- potential hang due to mutex deadlock
- “last message repeated n times” message was missing hostname

See the complete [changelog](http://www.rsyslog.com/changelog-for-6-2-2-v6-stable/).
