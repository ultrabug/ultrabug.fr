---
title: "Switching from Xchat to HexChat"
date: "2013-03-05"
categories: 
  - "linux"
tags: 
  - "hexchat"
  - "irc"
  - "xchat"
---

As [polynomial-c announced last year](http://www.gossamer-threads.com/lists/gentoo/dev/263232?do=post_view_threaded), xchat upstream is dead for some time now. Fortunately for us the fork **hexchat** is taking over and is compatible with your current xchat configuration so it's really easy to migrate.

## migrating to hexchat

$ mv .xchat2/ .config/hexchat/
$ mv .config/hexchat/xchat.conf .config/hexchat/hexchat.conf

As mentioned in the comments by Louis Tim Larsen, if you have some servers configured with more than one channel make sure to run this command as well :

sed -i 's/,#/\\nJ=#/g' ~/.config/hexchat/servlist.conf

Then run hexchat as you would xchat.

## theme your IRC

If like me you're a fan of [Solarized](http://ethanschoonover.com/solarized), you can get hexchat to use these colors thanks to some contributed [themes](http://hexchat.org/themes.html). Here's the quick hack to have it done, for the _Solarized Light_ theme.

$ cd .config/hexchat
$ wget http://dl.hexchat.org/themes/Solarized%20Light.hct
$ unzip -o Solarized\\ Light.hct

Restart hexchat and enjoy your up to date and colorized IRC client.
