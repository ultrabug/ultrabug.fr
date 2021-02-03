---
title: "After vacation bug hunting"
date: "2014-05-04"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
---

Two weeks vacations always seem short yet the 900+ mails waiting for sorting on my Gentoo Linux inbox was a reminder that our beloved distribution is well alive ! So I guess it was time for a little bug killing spree :)

## rabbitMQ v3.3.0

This release improves performance in a variety of conditions, adds monitoring information to identify performance bottlenecks, adds dynamically manageable shovels, and allows Java-based clients to reconnect automatically after network failure.

This release also corrects a number of defects in the broker and plugins, as well as introducing a host of smaller features as you can see on the [changelog](http://www.rabbitmq.com/release-notes/README-3.3.0.txt). **Be warned** that the [behavior of the guest user has been altered](http://www.rabbitmq.com/access-control.html) !

I also fixed a long awaiting bug to bump the [rabbitMQ C client to v0.5.0](https://bugs.gentoo.org/show_bug.cgi?id=480962)

## redis v2.8.9

Johan Bergström is as always doing a great and helpful job and is [actively working on redis](https://bugs.gentoo.org/show_bug.cgi?id=508456), thanks mate !

- \[NEW\] The HyperLogLog data structure. You can [read more about it](http://antirez.com/news/75) [ in this blog post](http://antirez.com/news/75)
- \[NEW\] The Sorted Set data type has now support for lexicographic range queries, check the new commands ZRANGEBYLEX, ZLEXCOUNT and ZREMRANGEBYLEX, which are documented at http://redis.io

## py3status v1.5

- fixes installation via pip
- added a --version command line argument to get the currently installed version of py3status

## upcoming bumps

You might be interested in what's next on the todo list :

- With the help of Thomas D. aka @Whissi, we're working on bumping and enhancing [**rsyslog** to v7.6.3](https://bugs.gentoo.org/show_bug.cgi?id=501988). For this a series of its dependencies have been bumped today as well.
- [**mongoDB** v2.6.0](https://bugs.gentoo.org/show_bug.cgi?id=508190) is also on track, as usual the guys @mongodb have broken the scons building so it's taking more time than it should to fix this hell (all help appreciated).
