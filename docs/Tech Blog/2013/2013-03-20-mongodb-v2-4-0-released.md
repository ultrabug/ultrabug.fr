---
title: "mongoDB : v2.4.0 released"
date: "2013-03-20"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "release"
---

A [few months ago](http://www.ultrabug.fr/coming-soon-on-mongodb/), I pointed out what was coming with this release and did [an update](http://www.ultrabug.fr/mongodb-2-4-0-rc/) of this cooking 2.4.0 later. Yesterday, 10gen announced the [release of the new stable branch of mongoDB v2.4.0](http://blog.mongodb.org/post/45754637343/mongodb-2-4-released). Instead of talking about it again, I'll focus on what this release brings to Gentoo users as I'm glad to announce that it's already available in portage.

## SSL support

First of all, I think it was a good time to close [bug #421289](https://bugs.gentoo.org/show_bug.cgi?id=421289) and finally enable the SSL support via the **ssl USE flag**. I'll support it as much as upstream does, so don't expect some big magic about it.

## Shared client library

Since this has always been a mess, I also added the **sharedclient USE flag** so that users who really need the client shared library can toggle its installation easily. This also permits me to isolate possible problems from the main ebuild.

## Upgrading to 2.4

This is seamless **unless you're running a sharded cluster** ! In this case, take great care of what you do and note that the upgrade is **only possible if your cluster is running v2.2** ! Please read with care the [upgrade plan](http://docs.mongodb.org/manual/release-notes/2.4-upgrade/).
