---
title: "RIP stabber"
date: "2013-11-27"
categories: 
  - "linux"
tags: 
  - "gentoo"
---

Today we did shutdown the oldest **Gentoo Linux server** of our oldest production datacenter. It was running since April, 5th of year 2006 so that's a total of **2793 days** of production level service as a stateful firewall. Its name was [**stabber**](http://eve.wikia.com/wiki/Stabber), in reference of a vessel in the Eve Online MMORPG which I played a lot at the time.

Our company has been running on Gentoo Linux since 2004 for its Linux platforms and I often hear and experience the astonishment of the other persons I speak to about this : "_Gentoo Linux in production, really ?"_ or _"Wow you guys are a bunch of crazy hardcore Gurus"_...

As if Gentoo Linux did not meet the production level requirements or the security level you expect from another major (usually not free) distribution and as if you had to master some major skills to have it done...

7 years later, stabber is in my opinion a proof that all those assumptions are wrong.

- I was a junior sysadmin at the time I made this server, we didn't want to pay for having a proper firewall so we decided to make our own (that's what Gentoo is to me : simple things done right, no added sugar)
- The **rolling updates of Gentoo did not brake our system** and it evolved along our infrastructure
- The **GLSA kept our server immune to security breaches** over the years (thx to the Gentoo security team)
- This server/firewall **passed the security tests of both Paypal and Ebay**, this looks production level enough to me

We did shutdown this server because it was a single point of failure on an old part of our architecture. Its role has been taken over by two fault tolerant servers/firewalls running... Gentoo Linux of course !

First _emerge.log_ entry

Wed Apr  5 12:53:22 2006 >>> sys-kernel/hardened-sources-2.6.14-r5

Latest _uname -a_

Linux stabber 2.6.16-hardened-r11 #1 SMP PREEMPT Wed Aug 30 15:51:49 CEST 2006 i686 Intel(R) Xeon(TM) CPU 3.20GHz GenuineIntel GNU/Linux

Latest _commands_

stabber ~ # echo "je taime" >> last.letter
stabber ~ # shutdown now -h

Dear fellow Gentoo Linux developers, your work makes all this possible, **thank you** !
