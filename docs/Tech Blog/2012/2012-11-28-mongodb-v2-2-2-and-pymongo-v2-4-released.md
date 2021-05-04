---
title: "mongoDB v2.2.2 and pymongo v2.4 released"
date: "2012-11-28"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "portage"
  - "pymongo"
  - "release"
---

## mongodb-2.2.2

This is a bugfix release of mongoDB, there is nothing major to note about it so just have a look at the [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/11886).

## pymongo-2.4

Ok here's a bigger cake we'll have to focus on as **you will have to adapt your code** to use it properly. Don't be scared, upgrading will not instantly break your current apps but...

### Connection / ReplicaSetConnection deprecation

Those classes are still available and provide the old _safe=False_ behavior meaning that by default, operations are not acknowledged. They are being replaced by **MongoClient** and **MongoReplicaSetClient** classes which on the contrary do acknowledge operations by default. So yes, **now your operations will run with a safe=True by default** !

### Write concern

In the mongoDB talks we never hear about safe writes but about write concerns. A new API now handles these operations' behavior such as fsync / journal committing / write acknowledgment which is in line with the internals of mongoDB. I think it's more clear and straightforward to handle this that way so it's a good job done by upstream even if it means we have to adapt our code for it. They come in the number of four options which are applied on a [**database or collection level**](http://api.mongodb.org/python/2.4/api/pymongo/collection.html#pymongo.collection.Collection.write_concern) :

- **w** **\= integer** : A value of 0 means we don't care so it's the fire-and-forget behavior we knew as safe=False. A value > 0 is the equivalent of the safe=True but with a more fine tuning on how many servers should confirm the operation.
- **wtimeout = integer** : Adds a timeout on the w parameter.
- **j = bool** : Wait until the operation has been committed to the journal.
- **fsync = bool** : Wait until the database to fsync all files to disk.

###  Highlights

- Cursor can be copied with functions from the copy module
- The set_profiling_level() method now supports a slow_ms option

See the rest in the full [changelog](http://api.mongodb.org/python/2.4/changelog.html).
