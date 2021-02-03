---
title: "rsyslog : new v6 branch in portage"
date: "2012-06-01"
categories: 
  - "linux"
tags: 
  - "ebuild"
  - "gentoo"
  - "release"
  - "rsyslog"
---

The first ebuild of the v6.2 stable branch of **rsyslog** is finally available in portage. This branch provides functional and performance enhancements of rsyslog.

# Quick highlights :

- Hadoop (HDFS) support has been considerably speeded up by supporting batched insert mode.
- TCP transmission overhead for TLS has been dramatically improved.
- TCP supports input worker thread pools.
- Support of log normalization via liblognorm rule bases. This permits very high performance normalization of semantically equal messages from different devices (and thus in different syntaxes).

Interesting upcoming features such as [mongoDB support and the enhanced config language are on the way with v6.4](http://bugzilla.adiscon.com/show_bug.cgi?id=330). Stay tuned !
