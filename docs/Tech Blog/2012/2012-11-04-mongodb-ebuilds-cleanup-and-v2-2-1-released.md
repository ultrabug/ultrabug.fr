---
title: "mongoDB : ebuilds cleanup and v2.2.1 released"
date: "2012-11-04"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "mongodb"
  - "nosql"
  - "portage"
  - "release"
---

Another bug killing spree has happened :) I'm glad to have closed quite a bunch of bugs related to mongoDB today.

## No more spidermonkey-1.7 dependency

Thanks to the help from [Ian Stakenvicius](https://bugs.gentoo.org/show_bug.cgi?id=390631), we managed to drop the spidermonkey-1.7 dependency and use the embedded version shipped in the sources. I extended this fix to all 2.0.x and 2.2.x ebuilds, the only package remaining is the one for v1.8.5 but it will be dropped soon.

## Newer boost compatibility

Boost-1.50 introduced a new filesystem v3 version while breaking compatibility with older v2 filesystems. [This broke mongoDB compilation](https://bugs.gentoo.org/show_bug.cgi?id=425190) for the guys running unstable version of boost. As I didn't want to force stable users to keyword their boost versions, I kept a version of each 2.x series compatible with v2 <boost-1.50 filesystem.

- <dev-libs/boost-1.50 users should use the ebuilds revisions 1 (-r1)
- \>=dev-libs/boost-1.50 users should use the ebuilds revisions 2 (-r2)

## v2.2.1 version bump

Last but not least, the new v2.2.1 is also available but only for >=boost-1.50 users. This is a nice bugfix release which you should consider to apply since it's the first of the 2.2 series.

See the full [changelog](https://jira.mongodb.org/secure/IssueNavigator.jspa?reset=true&jqlQuery=project+%3D+SERVER+AND+fixVersion+%3D+%222.2.1%22+AND+status+%3D+Resolved+ORDER+BY+priority+DESC&mode=hide).
