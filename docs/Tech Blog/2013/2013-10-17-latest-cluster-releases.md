---
title: "Latest cluster releases"
date: "2013-10-17"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "keepalived"
  - "portage"
  - "release"
---

Now that I'm back I've bumped some of the sys-cluster packages. Users of keepalived will be interested in this since it was more than a year that upstream released a version.

## keepalived-1.2.8

This is a big and long awaited one. It features major enhancements, features and bug fixes. The [changelog](http://www.keepalived.org/changelog.html) is pretty huge but here are some quick points which I particularly liked (biased view warning) :

- Revisited the whole code to use posix declaration style
- Boon Ang fixed comparison of primary IP addresses. If a router in the master state receives an advertisement with priority equal to the local priority, it must also compare the primary IP addresses (RFC 3768, section 6.4.3). The code to handle this was comparing two IP addresses with different byte-ordering, **resulting in multiple routers in the master state**. This patches resolves the problem by converting the local primary IP address to network byte order for the comparison.
- Henrique Mecking fixed memory leak in libipvs
- Willy Tarreau and Ryan O'Hara add the ability to **use VRRP over unicast**. Unicast IP addresses may be specified for each VRRP instance with the 'unicast_peer' configuration keyword. When a VRRP instance has one or more unicast IP address defined, VRRP advertisements will be sent to each of those addresses. Unicast IP addresses may be either IPv4 or IPv6. If you are planing to use this option, ensure every ip addresses present in unicast_peer configuration block do not belong to the same router/box. Otherwise it will generate duplicate packet at reception point.

## crmsh-1.2.6

Many bug fixes with better performances for [this release](http://hg.savannah.gnu.org/hgweb/crmsh/file/crmsh-1.2.6/ChangeLog). This is quite impressive, good work upstream !

## corosync-2.3.2

This one is about supporting live config reloading and fix high CPU usage when idle. See the [release notes](https://github.com/corosync/corosync/wiki/Corosync-2.3.2-release-notes).

## Soon to come

The resource-agents v3.9.6 and cluster-glue v1.0.12 should be released by their upstream pretty soon, stay tuned.
