---
title: "Python : new zeroMQ and mongoDB drivers"
date: "2013-01-25"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "pymongo"
  - "python"
  - "release"
---

## pyzmq-2.2.0.1

This one is very interesting to me because the code from the mighty [gevent-zeromq](https://github.com/traviscline/gevent-zeromq) library which brought gevent support to pyzmq has been merged into it ! I find it very humble and positive for the Open Source community to see such merges and want to express my gratitude to [Travis Cline](https://github.com/traviscline) and the zeroMQ team for that.

Migrating is as easy as :

\# gevent-zeromq previous way
from gevent_zeromq import zmq

# pyzmq new way
from pyzmq.green import zmq

I strongly encourage you to read the [changelog](http://zeromq.github.com/pyzmq/changelog.html).

## pymongo-2.4.2

Bugfix release, the main point is that PyMongo will no longer select a replica set member for read operations that is not in primary or secondary state. Here is the [changelog](https://jira.mongodb.org/browse/PYTHON/fixforversion/12299).
