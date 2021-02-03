---
title: "mongoDB and Pacemaker recent bumps"
date: "2013-04-26"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "pacemaker"
  - "portage"
  - "release"
---

## mongoDB 2.4.3

Yet another [bugfix release](https://jira.mongodb.org/browse/SERVER/fixforversion/12426), this new stable branch is surely one of the most quickly iterated I've ever seen. I guess we'll wait a bit longer at work before migrating to 2.4.x.

## pacemaker 1.1.10\_rc1

This is the release of pacemaker we've been waiting for, fixing among other things, the ACL problem which [was introduced in 1.1.9](http://www.ultrabug.fr/follow-up-on-pacemaker-v1-1-9-and-updated-pacemaker-gui/). Andrew and others are working hard to get a proper 1.1.10 out soon, thanks guys.

Meanwhile, we (gentoo cluster herd) have been contacted by **@Psi-Jack** who has offered his help to follow and keep some of our precious clustering packages up to date, I wish our work together will benefit everyone !

All of this is live on portage, enjoy.
