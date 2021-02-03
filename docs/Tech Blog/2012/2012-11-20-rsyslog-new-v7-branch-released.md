---
title: "rsyslog : new v7 branch released"
date: "2012-11-20"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "release"
  - "rsyslog"
---

It's been a long time since I took care of the rsyslog package so bear with me for these quite huge version releases. The main thing to note is that I finally packaged the **new v7 branch** which is stamped "_stable for production_" by upstream. The **v5 branch is not supported anymore** unless you have a professional contract with Adiscon so I encourage you to read Rainer's [blog post](http://blog.gerhards.net/2012/10/new-v7v6-stable-v5-now-legacy.html).

 

## v7.2.2

Optimizations, code refactoring for way improved performances and a lot of new features are there. The v7 series bring a lot of changes and neat stuff to rsyslog as you can see on this [v5 vs v7 link](http://www.rsyslog.com/main-advantages-of-rsyslog-v7-vs-v5/). Here are some hints :

- Improved configuration language
- Improved execution engine
- Full support for structured logging and JSON-based log messages (I discussed this matter on a [previous post](http://www.ultrabug.fr/state-of-the-event-log-architecture-enhancements/))
- Ability to normalize legacy text log messages to JSON

The changelog is very long, so you can browse [this](http://www.rsyslog.com/tag/v7/) to find out more.

## v5.10.1 and v6.6.0

Those releases contain backports bugfixes (v5) and enhancements (v6) fixed on the v7 branch so if you're not ready to jump straight to the new version, you might consider updating your branch for a last time :)
