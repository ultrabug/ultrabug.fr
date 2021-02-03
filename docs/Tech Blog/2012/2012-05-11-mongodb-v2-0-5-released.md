---
title: "mongoDB : v2.0.5 released"
date: "2012-05-11"
categories: 
  - "linux"
tags: 
  - "mongodb"
  - "nosql"
  - "release"
---

This is a bug fix release of mongoDB, it is now live in portage as well.

+\*mongodb-2.0.5 (11 May 2012)
+
+  11 May 2012; Ultrabug <ultrabug@gentoo.org> -mongodb-2.0.3.ebuild,
+  -files/mongodb-2.0.3-fix-scons.patch, +mongodb-2.0.5.ebuild:
+  Version bump, generic mms-agent URL, drop old.
+

# Bug fix highlight :

- Inconsistent query results on large data and result sets
- Race during static destruction of CommitJob object

See the complete [changelog](https://jira.mongodb.org/browse/SERVER/fixforversion/11137).
