---
title: "RethinkDB on Gentoo Linux"
date: "2016-09-02"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "nosql"
  - "portage"
  - "release"
  - "rethinkdb"
---

[![2014-11-05-cat-instagram](images/2014-11-05-cat-instagram.png)](http://www.ultrabug.fr/rethinkdb-on-gentoo-linux/2014-11-05-cat-instagram/)

It was about time I added a **new package** to **portage** and I'm very glad it to be **RethinkDB and its python driver** !

- **dev-db/rethinkdb**
- **dev-python/python-rethinkdb**

For those of you who never heard about this database, I urge you to go about their [excellent website](https://rethinkdb.com/) and have a good read.

## Packaging RethinkDB

**RethinkDB** has been under my radar for quite a long time now and when they finally got serious enough about [high availability](https://rethinkdb.com/blog/2.1-release/) I also got serious about using it at work... and obviously _"getting serious" + "work"_ means packaging it for **Gentoo Linux** :)

Quick notes on packaging for Gentoo Linux:

- This is a C++ project so it feels natural and easy to grasp
- The configure script already offers a way of using system libraries instead of the bundled ones which is in line with Gentoo's QA policy
- The only grey zone about the above statement is the web UI which is used _precompiled_

RethinkDB has a few QA violations which the ebuild is addressing by modifying the sources:

- There is a configure.default which tries to force some configure options
- The configure is missing some options to avoid auto installing some docs and init scripts
- The build system does its best to guess the CXX compiler but it should offer an option to set it directly
- The build system does not respect users' CXXFLAGS and tries to force the usage of **\-03**

## Getting our hands into RethinkDB

At work, we finally found the excuse to get our hands into RethinkDB when we challenged ourselves with developing a quizz game for our booth as a sponsor of Europython 2016.

It was a simple game where you were presented a question and four possible answers and you had 60 seconds to answer as much of them as you could. The trick is that we wanted to create an interactive game where the participant had to play on a tablet but the rest of the audience got to see who was currently playing and follow their score progression + their ranking for the day and the week **in real time** on another screen !

Another challenge for us in the creation of this game is that we only used technologies that were new to us and even switched jobs so the backend python guys would be doing the frontend javascript et vice et versa. The stack finally went like this :

- Game quizz frontend : Angular2 (TypeScript)
- Game questions API : Go
- Real time scores frontend : Angular2 + autobahn
- Real time scores API : python 3.5 asyncio + autobahn
- Database : RethinkDB

As you can see on the stack we chose RethinkDB for its main strength : **real time updates pushed to the connected clients**. The real time scores frontend and API were bonded together using [autobahn](http://autobahn.ws/) while the API was using the [changefeeds](https://rethinkdb.com/docs/changefeeds/python/) (realtime updates coming from the database) and broadcasting them to the frontend.

## What we learnt about RethinkDB

- We're sure that we want to use it in production !
- The [ReQL query language](https://rethinkdb.com/docs/introduction-to-reql/) is a pipeline so its syntax is quite tricky to get familiar with (even more when coming from mongoDB like us), it is as powerful as it can be disconcerting
- Realtime changefeeds have limitations which are sometimes not so easy to understand/find out (especially the order_by / secondary index part)
- Changefeeds limitations is a constraint you have to take into account in your data modeling !
- Changefeeds + order_by can do the ordering for you when using the **include_offsets** option, this is amazing
- The administration web UI is awesome
- The python 3.5 [asyncio proper support is still not merged](https://github.com/rethinkdb/rethinkdb/pull/5354), this is a pain !

## Try it out

Now that you can **emerge rethinkdb** I encourage you to try this awesome database.

Be advised that the ebuild also provides a way of configuring your rethinkdb instance by running **emerge --config dev-db/rethinkdb** !

I'll now try to get in touch with upstream to get [Gentoo listed on their website](https://rethinkdb.com/docs/install/).
