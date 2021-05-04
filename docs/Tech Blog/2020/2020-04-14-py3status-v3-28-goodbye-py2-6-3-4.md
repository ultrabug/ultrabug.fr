---
title: "py3status v3.28 - goodbye py2.6-3.4"
date: "2020-04-14"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "py3status"
  - "release"
---

The newest version of **py3status** starts to enforce the deprecation of Python 2.6 to 3.4 (included) initiated by [Thiago Kenji Okada](https://github.com/thiagokokada) more than a year ago and orchestrated by [Hugo van Kemenade](https://github.com/hugovk) via [#1904](https://github.com/ultrabug/py3status/pull/1904) and [#1896](https://github.com/ultrabug/py3status/pull/1896).

Thanks to Hugo, I discovered a nice tool by @[asottile](https://github.com/asottile) to update your Python code base to recent syntax sugars called [pyupgrade](https://github.com/asottile/pyupgrade/)!

Debian buster users might be interested in the installation war story that @[TRS-80](https://github.com/TRSx80) kindly described and the final (and documented) solution found.

## Changelog since v3.26

- drop support for EOL Python 2.6-3.4 (#1896), by Hugo van Kemenade
- i3status: support read_file module (#1909), by @lasers thx to @dohseven
- clock module: add "locale" config parameter to change time representation (#1910), by inemajo
- docs: update debian instructions fix #1916
- mpd_status module: use currentsong command if possible (#1924), by girst
- networkmanager module: allow using the currently active AP in formats (#1921), by Benoît Dardenne
- volume_status module: change amixer flag ordering fix #1914 (#1920)

## Thank you contributors

- Thiago Kenji Okada
- Hugo van Kemenade
- Benoît Dardenne
- @dohseven
- @inemajo
- @girst
- @lasers
