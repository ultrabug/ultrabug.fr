---
title: "uWSGI, gevent and pymongo 3 threads mayhem"
date: "2015-05-13"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "pymongo"
  - "python"
  - "uwsgi"
---

This is a quick heads-up post about a behaviour change when running a **gevent** based application using the new **pymongo 3** driver under **uWSGI** and its gevent loop.

I was naturally curious about testing this brand new and major update of the python driver for mongoDB so I just played it dumb : update and give a try on our existing code base.

The first thing I noticed instantly is that a vast majority of **our applications were suddenly unable to reload gracefully** and were force killed by uWSGI after some time !

worker 1 (pid: 9839) is taking too much time to die...NO MERCY !!!

## uWSGI's gevent-wait-for-hub

All our applications must be able to be gracefully reloaded at any time. Some of them are spawning quite a few greenlets on their own so as an added measure of making sure we never loose any running greenlet we use the **gevent-wait-for-hub** option, which is described as follow :

wait for gevent hub's death instead of the control greenlet

... which does not mean a lot but is explained in a previous uWSGI changelog :

During shutdown only the greenlets spawned by uWSGI are taken in account,
and after all of them are destroyed the process will exit.

This is different from the old approach where the process wait for
ALL the currently available greenlets (and monkeypatched threads).

If you prefer the old behaviour just specify the option gevent-wait-for-hub

## pymongo 3

Compared to its previous 2.x versions, one of the overall key aspect of the new pymongo 3 driver is its intensive usage of **threads** to handle server discovery and connection pools.

Now we can relate this very fact to the _gevent-wait-for-hub_ behaviour explained above :

the process wait for ALL the currently available greenlets
(**and monkeypatched threads**)

This explained why our applications were hanging until the **reload-mercy** (force kill) timeout option of uWSGI hit the fan !

## conclusion

When using **pymongo 3** with the **gevent-wait-for-hub** option, you have to keep in mind that all of pymongo's threads (so monkey patched threads) are considered as active greenlets and will thus be waited for termination before uWSGI recycles the worker !

Two options come in mind to handle this properly :

1. stop using the **gevent-wait-for-hub** option and change your code to use a **[gevent pool group](http://www.gevent.org/gevent.pool.html#gevent.pool.Group)** to make sure that all of your important greenlets are taken care of when a graceful reload happens (this is how we do it today, the gevent-wait-for-hub option usage was just over protective for us).
2. modify your code to **properly close all your pymongo connections** on graceful reloads.

Hope this will save some people the trouble of debugging this ;)
