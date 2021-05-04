---
title: "Drop-down terminal in i3"
date: "2013-10-25"
categories: 
  - "linux"
tags: 
  - "drop-down"
  - "gentoo"
  - "i3"
  - "i3wm"
  - "terminal"
---

One of the reasons I switched from KDE to i3wm is that I love and need terminals. In my field of work you happen to spawn dozens of them and you always end up running out of space / workspaces.

**Yakuake** has been a real ally to me for years as I intensively use a drop-down terminal for sporadic usages. It is hard to match Yakuake's efficiency and ability to split terminals but I couldn't stand all those KDE dependencies anymore; I had to find a great drop-down terminal solution in i3.

So I started looking at other drop-down terminals such as _Terra_ and _Guake_ but they didn't fit my **low dependencies and features** list requirements.

## Drop-down Terminator

My current solution is to take advantage of the **floating mode of i3**, use it with my beloved **terminator** et voilà ! Nothing more to install, no extra dependency, using the same shortcuts of my main $TERMINAL and all of its features :)

The idea is simple, we'll create a special profile in terminator and have it spawned in floating mode upon i3 start. This profile must cover the following drop-down behaviors :

- respond to a configurable show/hide key binding
- present a drop-down terminal at the center of the screen
- the interface should be dead simple and efficient and support splitting

Just edit your terminator configuration in _**~/.config/terminator/conf**_ and add :

[keybindings]
  hide_window = F1

Then add the _dropdown_ profile under the [profiles] section :

[profiles]
[[dropdown]]
  exit_action = close
  scrollback_lines = 10000
  background_image = None
  scroll_on_output = False
  show_titlebar = False

That's my minimal config, you can add your own stuff to it as well. Now we only need to configure i3 to spawn this profile at login and have it in floating mode.

Modify your i3 config file, usually **~/.i3/config** :

exec terminator -c dropdown -p dropdown -T "Le Terminator" -H --geometry=1550x800

for_window [class="Terminator" instance="dropdown"] floating enable

That's as simple as this.

EDIT: as per Joe's comment, you can also configure i3 to place your floating Terminator window wherever you want (in his case, top off the screen). This still goes into your i3 config from above :

for_window [class=”Terminator” instance=”dropdown”] floating enable move absolute position 0 0

There's still one limitation which I didn't come across yet :

- Unlike Yakuake, our drop-down terminator has a fixed geometry which you must set in the i3 config above and does not support percentage values. So if you have multiple screens of different resolutions it won't adapt on them based on the screen you want to show your drop-down terminator.

So long, Yakuake !
