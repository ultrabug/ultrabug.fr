---
title: "mongoDB : latest releases"
date: "2013-06-05"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "pymongo"
  - "release"
---

## mongodb-2.4.4

Just bumped it to portage and fixed an open bug along. This is yet another bugfix release which backports the switch to the Cyrus SASL2 library for sasl authentication (kerberos). Dependencies were adjusted so you no longer need libgsasl on your systems (remember to depclean).

### highlights

- config upgrade fails if collection missing "key" field
- migrate to Cyrus SASL2 library for sasl authentication
- rollback files missing after rollback

## pymongo-2.5.2

This one is important to note and **I strongly encourage you to upgrade asap** as it fixes an important [security bug](https://bugs.gentoo.org/show_bug.cgi?id=472034) (CVE-2013-2132). I've almost dropped all other versions from tree anyway...

### highlights 2.5.x

- support GSSAPI (kerberos) authentication
- support for SSL certificate validation with hostname matching
- support for delegated and role based authentication

## mongodb-2.5.x dev

What's cooking for the next 2.6 releases ? Let's take a quick look as of today.

- background indexing on secondaries (hell yes!)
- new implementation of external sort
- add support for building from source with particular C++11 compilers (will fix a gentoo bug reported quite a long time ago)
- mongod automatically continues in progress index builds following restart
