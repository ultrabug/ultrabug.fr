---
title: "pacemaker v1.1.10 & corosync v2.3.1"
date: "2013-09-03"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "pacemaker"
  - "portage"
  - "release"
---

More than 5 months since the last bump of pacemaker. I'm glad that @beekhof did release the final pacemaker-1.1.10 and that the officially stable corosync got bumped to 2.3.1.

The changelogs are quite heavy so I won't go into details about them but they both have quite a nice bunch of bugfixes and compatibility features. That's why I'm hoping we should soon be able to [fix bug #429416](https://bugs.gentoo.org/show_bug.cgi?id=429416#c14) and drop corosync hard mask. Hopefully some users such as **@pvsa** will give us some valuable feedback which will allow us to do it smoothly.

## changelog

- [pacemaker-1.1.10](https://github.com/ClusterLabs/pacemaker/blob/master/ChangeLog)
- [corosync-2.3.1](https://github.com/corosync/corosync/wiki/Corosync-2.3.1-Release-Notes)
