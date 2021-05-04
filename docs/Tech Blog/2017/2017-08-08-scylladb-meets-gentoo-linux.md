---
title: "ScyllaDB meets Gentoo Linux"
date: "2017-08-08"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "nosql"
  - "portage"
  - "scylla"
---

![](images/mascot-1.png)I am happy to announce that my work on packaging **ScyllaDB for Gentoo Linux** is complete!

Happy or curious users are very welcome to share their thoughts and ping me to get it into portage (which will very likely happen).

## Why Scylla?

Ever heard of the Cassandra NoSQL database and Java GC/Heap space problems?... if you do, you already get it ;)

I will not go into the details as [their website](http://www.scylladb.com/product/) does this way better than me but I got interested into **Scylla** because **it fits the Gentoo Linux philosophy** very well. If you remember my [writing about packaging Rethinkdb for Gentoo Linux](http://www.ultrabug.fr/rethinkdb-on-gentoo-linux/), I think that we have a great match with Scylla as well!

- **it is written in C++** so it plays very well with emerge
- **the code quality is so great** that building it does not require heavy patching on the ebuild (feels good to be a packager)
- **the code relies on system libs** instead of bundling them in the sources (hurrah!)
- **performance tuning is handled by smart scripting and automation**, allowing the relationship between the project and the hardware is strong

I believe that these are good enough points to go further and that such a project can benefit from a source based distribution like Gentoo Linux. Of course compiling on multiple systems is a challenge for such a database but one does not improve by staying in their comfort zone. ![](images/2017-08-08-142318_158x79_scrot-150x79.png)

## Upstream & contributions

Packaging is a great excuse to get to know the source code of a project but more importantly the people behind it.

So here I got to my first contributions to Scylla to get Gentoo Linux as a detected and supported Linux distribution in the different scripts and tools used to automatically setup the machine it will run upon (fear not, I contributed bash & python, not C++)...

Even if I expected to contribute using Github PRs and got to change my habits to a [git-patch+mailing list combo](https://github.com/scylladb/scylla/blob/master/CONTRIBUTING.md), I got warmly welcomed and received positive and genuine interest in the contributions. They got merged quickly and thanks to them you can install and experience Scylla in Gentoo Linux without heavy patching on our side.

**Special shout out to Pekka, Avi and Vlad** for their welcoming and insightful code reviews!

I've some open contributions about pushing further on the python code QA side to get the tools to a higher level of coding standards. Seeing how upstream is serious about this I have faith that it will get merged and a good base for other contributions.

Last note about reaching them is that I am a bit sad that **they're not using IRC** freenode to communicate (I instinctively joined #scylla and found myself alone) but [they're on Slack](https://join.slack.com/t/scylladb-users/shared_invite/MjExNjI4NTY4NTMxLTE0OTk4NjU3NjUtNjcwZDZjNmQwZg) (those "modern folks") and pretty responsive to the [mailing lists](http://www.scylladb.com/open-source/) ;)

## Java & Scylla

Even if scylla is a rewrite of Cassandra in C++, the project still relies on some external tools used by the Cassandra community which are written in Java.

When you install the scylla package on Gentoo, you will see that those two packages are Java based dependencies:

- app-admin/scylla-tools
- app-admin/scylla-jmx

It pained me a lot to package those (thanks to help of @monsieurp) but they are building and working as expected so this gets the packaging of the whole Scylla project pretty solid.

## emerge dev-db/scylla

**The scylla packages are located in the [ultrabug overlay](https://gitweb.gentoo.org/dev/ultrabug.git/)** for now until I test them even more and ultimately put them in production. Then they'll surely reach the portage tree with the approval of the Gentoo java team for the app-admin/ packages listed above.

I provide a live ebuild (scylla-9999 with no keywords) and ebuilds for the latest major version (2.0_rc1 at time of writing).

It's as simple as:

$ sudo layman -a ultrabug
$ sudo emerge -a dev-db/scylla
$ sudo emerge --config dev-db/scylla

**Try it out and tell me what you think**, I hope you'll start considering and using this awesome database!
