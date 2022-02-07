---
title: "keepalived v1.2.11 & glusterfs v3.4.2"
date: "2014-01-31"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "glusterfs"
  - "keepalived"
  - "portage"
  - "release"
---

Quick post for two quick bumps related to clustering.

## glusterfs-3.4.2

- quite a lot of [bug fixes and improvements](https://github.com/gluster/glusterfs/blob/release-3.4/doc/release-notes/3.4.2.md)
- contains a backport for libgfapi support for integrating with NFS Ganesha
- nfs/mount3: fix crash in subdir resolution

## keepalived-1.2.11

- autoconf: better libnl3 detection
- Fix memory allocation for MD5 digest
- Quite some nice memory leak fixes on different components
- vrrp: dont try to load ip_vs module when not needed
- Pim van den Berg work on libipvs-2.6 to sync with libipvs from ipvsadm 1.27
- vrrp: extend ip parser to support default and default6
- vrrp: fix/extend gratuitous ARP handling (multiple people reported issues where MASTER didn't recover properly after outage due to no gratuitous ARP sent)
- Multiple fixes to genhash
- vrrp: fix vrrp socket sync while leaving FAULT state (old old bug here)
- Full [changelog here](http://www.keepalived.org/changelog.html)
