---
title: "Meet py3status"
date: "2013-02-21"
categories: 
  - "linux"
tags: 
  - "i3wm"
  - "py3status"
  - "python"
---

_This is the first public release of one of my open-source projects, don't hesitate to share some feedback and/or thoughts with me._

## Background

As a sysadmin, I have **a lot** of consoles open on multiples desktops and my 30" screen was still not enough to cover my needs. To make things short, I needed to spare every pixel I could and KDE was really frustrating me as it was wasting a lot of space and ran quite a bunch of useless stuff in the background (akonadi/nepomuk anyone ?).

Then came my cyclic rage about it and I finally found _my precious_ : [i3wm](http://i3wm.org). I just love it as it is what I ever needed : a lightweight yet very functional and handy WM.

- No more resizing my consoles to fit next to each other and I can still use floating windows for the needed applications.
- No more huge and pixel-hungry task bar, just a simple and very efficient one.

### customization

The problem when you start using something new and awesome is that you get a lot of ideas on what you could do with it and how you'd love to customize it. I mean, when using KDE or Gnome, your ideas are quickly shaped by the fact that you'd have to learn some exotic framework or language to implement them.

- Did you ever ask yourself how to add your own stuff in your task bar on KDE or Gnome ?

- What if the customization options you want are not available in your WM menus ?

Well, my answer was "never mind" tbh and I slowly even lost the idea of implementing anything on my task bar.

### i3bar & i3status

After switching to i3wm, my first customization was to name my workspaces and setup my own colors to adjust the look & feel of my desktop. Then I started to tune the program responsible for displaying useful information on my bar : [**i3status**](http://i3wm.org/i3status/). As you may know, you have some limited modules which can take care of displaying some useful information on your bar such as the free disk space on a disk partition or your wired/wireless network status.

But then I asked myself the same questions as I used to on my KDE days : what if I want more ? my own stuff on my task bar ?

## Introducing py3status

Thanks to the **i3bar** open and simple protocol and the robust (even if somewhat limited) **i3status** program, I could finally [hack into my bar](https://faq.i3wm.org/question/459/external-scriptsprograms-in-i3status-without-loosing-colors/). Naturally, I had to do it myself and there was a few examples available on the net but nothing really handy and extensible enough. That's how I had the idea of developping **[py3status](https://github.com/ultrabug/py3status/wiki)** !

### philosophy & goals

- **no extra configuration file needed**
- rely on i3status and its **existing configuration** as much as possible
- **be extensible**, it must be easy for users to add their own stuff/output by writing a simple python class which will be loaded and executed dynamically
- add some built-in enhancement/transformation of basic i3status modules output

### available now on github

I'm glad to announce that [I pushed it today on github](https://github.com/ultrabug/py3status) ! You can start using **[py3status](https://github.com/ultrabug/py3status)** now and give your feedback. I hope this project will help users get more of their i3wm environment and encourage their hacking power !
