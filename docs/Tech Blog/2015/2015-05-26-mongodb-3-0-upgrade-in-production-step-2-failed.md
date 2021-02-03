---
title: "MongoDB 3.0 upgrade in production : step 2 failed"
date: "2015-05-26"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
---

In [my previous post](http://www.ultrabug.fr/mongodb-3-0-upgrade-in-production-first-steps/) regarding the **migration of our production cluster to mongoDB 3.0** WiredTiger, we successfully upgraded all the secondaries of our replica-sets with decent performances and (almost, read on) no breakage.

## Step 2 plan

The next step of our migration was to test our work load on WiredTiger primaries. After all, this is where the new engine would finally demonstrate all its capabilities.

- We thus scheduled a step down from our 3.0 MMAPv1 primary servers so that our WiredTiger secondaries would take over.
- Not migrating the primaries was a safety net in case something went wrong... **And boy it went so wrong we're glad we played it safe that way !**
- **We rolled back** after 10 minutes of utter bitterness.

## The failure

After all the wait and expectation, I can't express our level of disappointment at work when we saw that the WiredTiger engine could not handle our work load. Our application started immediately to throw 50 to 250 **WriteConflict** errors per minute !

Turns out that we are affected by [this bug and that, of course, we're not the only ones](https://jira.mongodb.org/browse/SERVER-18213). So far it seems that it affects collections with :

- heavy insert / update work loads
- an unique index (or compound index)

## The breakages

We also discovered that we're affected by a weird **mongodump** new behaviour where [**the dumped BSON file does not contain the number of documents**](https://jira.mongodb.org/browse/TOOLS-750) that mongodump said it was exporting. This is clearly a new problem because it happened **right after all our secondaries switched to WiredTiger**.

Since we have to ensure a strong consistency of our exports and that the mongoDB guys don't seem so keen on moving on the bug (which I surely can understand) there is a large possibility that **we'll have to roll back even the WiredTiger secondaries** altogether.

Not to mention that since the 3.0 version, we experience some CPU overloads crashing the entire server on our MMAPv1 primaries that we're still trying to tackle before opening another JIRA bug...

## Sad panda

Of course, any new major release such as 3.0 causes its headaches and brings its lot of bugs. We were ready for this hence the safety steps we took to ensure that we could roll back on any problem.

But as a long time advocate of mongoDB I must admit my frustration, even more after the time it took to get this 3.0 out and all the expectations that came with it.

I hope I can share some better news on the next blog post.
