---
title: "The mongoDB 2.2 era"
date: "2012-08-30"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "release"
---

Yesterday MongoDB entered the version 2.2 era with all its long time awaited [new features](http://blog.mongodb.org/post/30451575525/mongodb-2-2-released). For the strong MongoDB fans across the world, those features were known and expected because some of them were requested for quite long now. They often were tested and debugged with 10gen before being released also, that's the way it goes.

In mongoParis 2012, I took the chance to discuss a few matters with a 10gen engineer about some of those new features and he predicted that the release would take place in September. He was not far from the truth and I'm glad that for once a release is launched before what I was expecting (even if mongo jira was even more optimistic). My main points in this discussions and his answers were :

- Will they take the chance to drop the spidermonkey 1.7 requirement and finally move their code to use v1.8 ?

> _No, they'd rather focus on switching over to the v8 javascript engine, even if it's a long time goal. They're still not satisfied with the current v8 stability regarding locks so it's not suited for production yet._

- Will the new aggregation framework be capable of handling "join" like requests ?

> _No, that's not what it was designed for yet._

- What about the output of the new aggregation framework, can we write it into a collection or is it RAM only (thus limiting the result set size) ?

> _The result set is RAM only so we have the same limitations as a distinct command : 16MB. We plan on being able to store the output on a collection or something later._

I must admit, for my planned use cases the last answer was a head shot on the aggregation framework but I still think it's a remarkable achievement and I can only say 10gen did a good job and thank them for releasing it.

# mongodb-2.2.0

My thoughts on this new release are clouded with both my intensive administrator point of view (our main DB is over 2,5 billions documents large) and my packager point of view (Gentoo Linux). I'll start with my packager pov, which is bad unfortunately :

- I am annoyed by their stubbornness with sticking to spidermonkey-1.7. Hell, it's not like the community didn't do the work for them already : Fedora do provide a working spidermonkey-1.8 patch for mongoDB. I may reconsider using it for the mongodb-2.2.0 series if they update their patch again.
- I am not happy with them not being strict in their compile-from-source procedure. Scons sucks but everything is arguable, what is not is that they don't seem to make some real efforts and testing on proper compilation. I feel like they neglect the people caring for the sources and not some pre-baked binary and it's not good imo because this is also a great field for optimizing your software.
- They gave me a headache debugging the 2.2.x release to make it compile fine. I won't go into too much details (I'll fill bugs for them) but hell, they say they provide a scons option --use-system-all which they don't even honor by hard sourcing spidermonkey-1.7 libraries from their own sources !
- They now use boost-1.49, I won't blame them here.

Now come the good news, at last, from my user perspective :

- No strong **[upgrade](http://docs.mongodb.org/manual/release-notes/2.2/#upgrading)** plan needed. Just upgrade the clients (mongos) first then roll on the servers, perfect.
- The **concurrency** improvements are just so awesome on paper : locks are now per database, not for the whole mongod process. This is good news if you have multiple databases, which I don't, but they also implemented a new subsystem which avoids locks on most page faulting operations so even I can benefit from this.
- The **aggregation framework** will simplify some queries we could only achieve using mapReduce and offer interesting possibilities for calculations such as statistics.
- **TTL** collections : those I have been waiting since mongoParis 2011. I have tons of ideas and use cases.
- _mongotop_ and _mongostat_ now support authentication while _mongodump_ can read from secondaries.
- We can now log to **syslog** instead of fixed log files using the --syslog command line argument to mongod.
- Lower migration thresholds ensure a better distribution of data for small collections on clusters.

See the full [changelog](http://docs.mongodb.org/manual/release-notes/2.2/) for all the details.

# pymongo-2.3

All drivers also had to adapt to be able to offer those new features and benefit from them. Apart from supporting the aggregation framework, I will highlight this change as it affects me potentially :

- Users of authentication must upgrade to PyMongo 2.3 (or newer) for “safe” write operations to function correctly.

Better be aware and safe than sorry mates, remember to update your drivers and read the [changelog](http://api.mongodb.org/python/2.3rc1/changelog.html#changes-in-version-2-3).

Those versions are already available in portage, you can stop reading and go compiling now.
