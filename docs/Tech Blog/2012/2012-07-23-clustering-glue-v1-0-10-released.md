---
title: "Clustering : glue v1.0.10 released"
date: "2012-07-23"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "portage"
  - "release"
---

The newly released cluster glue libraries for Pacemaker / Heartbeat are available in portage.

From my perspective, the major enhancement is that the clplumbing (the code responsible for passing along cib messages between nodes) now include compression. This was something [I reported upstream](https://developerbugs.linuxfoundation.org/show_bug.cgi?id=2633) a long time ago and I was handling with the large-cluster USE flag on the ebuild (I thus dropped it from IUSE).

## Highlights :

- Compression modules included and compression handling improved in clplumbing
- one memory leak fixed in clplumbing
- support for asynchronous I/O in sbd
