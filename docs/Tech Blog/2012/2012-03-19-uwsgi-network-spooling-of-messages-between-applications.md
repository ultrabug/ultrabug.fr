---
title: "uWSGI : network spooling of messages between applications"
date: "2012-03-19"
categories: 
  - "linux"
tags: 
  - "django"
  - "network-spooling"
  - "python"
  - "uwsgi"
---

One of the great new [uWSGI v1.1](http://lists.unbit.it/pipermail/uwsgi/2012-March/003838.html) features is network spooling of messages between applications. This short article demonstrates how to use it between a front end django app and a back end python app.

- [Download the fully packaged demo](http://www.ultrabug.fr/gentoo/uwsgi-spooler.tar.bz)

I advise you to use a uWSGI emperor and simply drop the provided ini files in its folder. The example is simple enough but here is an explanation of how it works.

1. The **sender** is a django app which you call via your browser, the front end.
2. The sender app uses the **mashal** module which permits to pass a type rich message (dictionary) through a string only spooling mechanism (yes, it's very handy).
3. The sender sends a **type 17 message (spool request message)** over the network providing the message.
4. The **receiver** app is a standalone spooling application written in standard python, this would be the back end.
5. The receiver just prints out what it received via the network spooling mechanism.

As I said, this is just an illustration of what can be done. You could look into [uwsgidecorators](http://projects.unbit.it/uwsgi/wiki/Decorators) and mix this with other stuff that suits your needs. Enjoy !
