---
title: "Couchbase on Gentoo Linux"
date: "2014-03-07"
categories: 
  - "linux"
tags: 
  - "couchbase"
  - "gentoo"
  - "nosql"
  - "portage"
---

Back in 2010 when I was comparing different NoSQL solutions I came across CouchDB. Even tho I went for mongoDB in the end, it was still a nice and promising technology even more since the merge with the Membase guys in late 2012 which lead to the actual **Couchbase**.

I won't go into the details of Couchbase itself since it's way covered all around the net but I wanted to let you guys know that I've packaged most of the couchbase ecosystem for Gentoo Linux :

- dev-db/**couchbase-server-community-2.2.0** : the community server edition (bin)
- dev-libs/**libcouchbase-2.2.0** : the C client library
- dev-python/**couchbase-1.2.0** : the python client library

Those packages are still only available on [my overlay](http://git.overlays.gentoo.org/gitweb/?p=dev/ultrabug.git;a=tree) (ultrabug on layman) since I'm not sure about the interest of other users in the community and I still need to make sure it's production ready enough.

If you're interested in seeing this package in portage, please say so !

_I dedicate this packaging to @atorgfr :)_
