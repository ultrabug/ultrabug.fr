---
title: "Follow-up on pacemaker v1.1.9 and updated pacemaker-gui"
date: "2013-03-15"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "portage"
  - "release"
---

In my [previous post](http://www.ultrabug.fr/pacemaker-vulnerability-and-v1-1-9-release/) I talked about a permission problem introduced in pacemaker-1.1.9 which requires root to be a member of the haclient group. I've been helping @beekhof to investigate on this and I'm glad [he found and fixed both the problem and a memory leak](https://github.com/beekhof/pacemaker/commit/3c9275e9ebdcb39ce58f73e62cef562d5dd6cb96) ! We're still investigating on another [issue](https://bugs.gentoo.org/show_bug.cgi?id=461698) but we should be seeing a new version bump pretty soon, thank you Andrew !

## pacemaker-gui v2.1.2

One of my colleagues recently complained that pacemaker-gui-2.1.1 was not compatible with newer pacemaker releases (>=1.1.8) so he had to install pacemaker-1.1.7 if he wanted to benefit from the GUI. I contacted [@gao-yan](https://github.com/ClusterLabs/pacemaker-mgmt) from SUSE who's the main upstream for this package and asked him for a tag bump. Here comes pacemaker-gui-2.1.2 which is compatible with all newer pacemaker releases ! Thanks again mate.
