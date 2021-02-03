---
title: "rsyslog : v7.4.4 released"
date: "2013-09-10"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "rsyslog"
---

**Contribution**. This must be what I love the most and one of the more rewarding thing in the Open Source community.

I always found it more natural with Gentoo as you're really close to the source code so we (devs and users) can see and propose fixes natively to upstream. I known some devs of cool upstreams (mongoDB) do use Gentoo on their developing box because of this close-to-source philosophy.

I don't know if Rainer does, but I'm glad our [contribution](http://bugzilla.adiscon.com/show_bug.cgi?id=438) (thx to @hwoarang) has been merged to the newer rsyslog. I'm glad to say that we now need no patch at all to build rsyslog on Gentoo !

Long time warning had been issued, I took the opportunity of this bump to **clean and drop older and unsupported versions of rsyslog**. The only stable branch remaining is v7 from now on. I also made a step towards [systemd integration](https://bugs.gentoo.org/show_bug.cgi?id=442706) thanks to @slyfox.

## highlights

- make rsyslog use the new json-c pkgconfig file if available. Thanks to the Gentoo team for the patches.
- bugfix: imfile parameter “persistStateInterval” was unusable due to a case typo in imfile; work-around was to use legacy config
- bugfix: slightly malformed SMTP handling in ommail
- bugfix: segfault in omprog if no template was provided (now dflt is used)
- bugfix: segfault in ompipe if no template was provided (now dflt is used)
- bugfix: segfault in omsnmp if no template was provided (now dflt is used)
- bugfix: some omsnmp optional config params were flagged as mandatory
