---
title: "uhashring : consistent hashing in python"
date: "2015-10-20"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "python"
---

It's been quite some time since I wanted to use a **consistent hashing** based distribution of my workload in a quite big cluster at work. So when we finally reached the point where this became critical for some job processing I rushed to find out what python library I could use to implement this easily and efficiently.

I was surprised not to find a clear "winner" for such a library. The more "popular" named _hash\_ring_ has a rather unoptimized source code and is dead (old issues, no answer). Some others stepped up since but with no clear interest for contributions and almost no added features for real world applications.

So I packaged the ketama C library and its python binding on my overlay to get intimate with its algorithm. Then I started working on my own pure python library and released **[uhashring](https://github.com/ultrabug/uhashring)** on Pypi and on **Gentoo** portage !

## **Features**

- **instance-oriented usage** so you can use your consistent hash ring object directly in your code (see [advanced usage](https://github.com/ultrabug/uhashring#advanced-usage)).
- a lot of **convenient methods** to use your consistent hash ring in real world applications.
- simple **integration** with other libs such as memcache through monkey patching.
- all the missing functions in the libketama C python binding (which is not even available on pypi).
- another and more performant consistent hash algorithm if you don't care about the ketama compatibility (see [benchmark](https://github.com/ultrabug/uhashring#benchmark)).
- native **pypy support**.
- tests of implementation, key distribution and ketama compatibility.

## **WTF ?**

Not so sure about **hash tables** and **consistent hashing** ? Read my [consistent hashing 101](http://www.ultrabug.fr/consistent-hashing-101/) explanation attempt !
