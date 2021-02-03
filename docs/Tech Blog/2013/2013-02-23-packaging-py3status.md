---
title: "Packaging py3status"
date: "2013-02-23"
categories: 
  - "linux"
tags: 
  - "py3status"
  - "python"
---

So I exchanged some mails with **Michael Stapelberg of i3wm** who rightly pointed out that my initial installation method of py3status was un-pythonic. I was not satisfied of using a bash setup either and I couldn't imagine a better opportunity to learn how to write a proper setup.py for my project.

Thanks to my Gentoo Linux packager experience, I knew what I had to do, so a few searchs and tests later I'm glad to announce that [py3status installation is standard](https://github.com/ultrabug/py3status#installation-non-gentoo-users) ! I of course also packaged [py3status for Gentoo Linux](https://github.com/ultrabug/py3status#installation-gentoo-users) users : meet [x11-misc/py3status on my overlay](http://git.overlays.gentoo.org/gitweb/?p=dev/ultrabug.git;a=tree;f=x11-misc/py3status;h=675792573f839ca460065a4cb68b2f3a4f8bdf79;hb=4559aabe8dd11242f33dd2dad1a0a6236c29b807).

**py3status** being a real command and not a simple python module, I had to find the way to have setuptools taking care of this for me. I was happy to find out that this is pretty easy and that it works on both Linux & Windows, it's awesome !

I will explain all this in one of my next blog post as I'm sure it can be of interest.
