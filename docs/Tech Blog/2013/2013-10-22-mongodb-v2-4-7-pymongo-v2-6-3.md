---
title: "mongoDB v2.4.7 & pymongo v2.6.3"
date: "2013-10-22"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "pymongo"
  - "release"
---

First of all, I'd like to point out a quite big change in the Gentoo mongodb package. The Chromium team responsible for the v8 package decided to [stop its maintenance](http://www.mail-archive.com/gentoo-dev@lists.gentoo.org/msg60838.html) as it was too much trouble to be used efficiently as a shared library (mainly due to upstream's breakage behavior). Even tho I don't like bundled libraries on sources, I understand my fellow developers point of view.

I've thus been asked and did **switch the mongodb ebuild to use the bundled v8 library**. This means that mongodb has no more v8 packaging dependency now. The **mongodb v2.2.x** users are advised that since upstream does not bundle the v8 lib in their source, I dropped the v8 USE flag and support altogether on this version (it's not officially supported anyway) !

This being said, I'll drop the old ebuilds from tree on the next releases iterations.

## mongodb-2.4.7

Yet another bugfix release on this unfamous 2.4.x series :

- Fixed over-aggressive caching of V8 Isolates
- Removed extraneous initial count during mapReduce
- Cache results of dbhash command
- Fixed memory leak in aggregation

## pymongo-2.6.3

BSON parser hardening and fixes in the connection pool mechanism. [More info here](http://emptysqua.re/blog/pymongo-2-6-3-released/).
