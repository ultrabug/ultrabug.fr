---
title: "Gevent : SSL support fixed for python 2.7.9"
date: "2015-05-23"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "gevent"
  - "python"
---

Good news for **gevent** users blocked on python < 2.7.9 due to [broken SSL support](https://github.com/gevent/gevent/issues/477) since python upstream [dropped the private API \_ssl.sslwrap](http://bugs.python.org/issue22438) that eventlet was using.

This issue was starting to get old and problematic since [GLSA 2015-0310](https://security.gentoo.org/glsa/201503-10) but I'm happy to say that almost 6 hours after the [**gevent-1.0.2 release**](https://github.com/gevent/gevent/issues/477#issuecomment-104888475), it is already available on portage !

We were also affected by this issue at work so I'm glad that the tension between ops and devs this issue was causing will finally be over ;)
