---
title: "mongoDB v2.4.1 and pymongo 2.5 released"
date: "2013-03-25"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "portage"
  - "release"
---

10gen released a **critical** update for mongoDB 2.4.0 which [affected queries](https://jira.mongodb.org/browse/SERVER-9087) on secondaries, **you should upgrade** asap. The python mongo driver followed the 2.4.x releases and got bumped to 2.5 this week-end. I am pleased to announce that I took the chance to add the **[kerberos authentication](http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication/) support** to both ebuilds while bumping them.

## pymongo-2.5

- GSSAPI (Kerberos) authentication
- SSL certificate validation with hostname matching
- Delegated and role based authentication
