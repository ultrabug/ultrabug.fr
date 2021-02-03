---
title: "Squid proxy : blocking download of some file extensions"
date: "2013-05-17"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "proxy"
  - "squid"
---

It is a common request in squid to have it **block downloading certain files based on their extension** in the url path. A quick look at google's results on the subject **apparently** gives us the solution to get this done easily by squid.

The common solution is to create an ACL file listing regular expressions of the extensions you want to block and then apply this to your **http\_access** rules.

## blockExtensions.acl

\\.exe$

## squid.conf

acl blockExtensions urlpath\_regex -i "/etc/squid/blockExtensions.acl"

\[...\]

http\_access allow localnet !blockExtensions

Unfortunately **this is not enough to prevent users from downloading .exe files.** The mistake here is that we assume that the URL will strictly finish by the extension we want to block, consider the two examples below :

http://download.com/badass.exe     // will be DENIED as expected

http://download.com/badass.exe?    // WON'T be denied as it does not match the regex !

Squid uses the _extended regex_ processor which is the same as egrep. So we need to change our blockExtensions.acl file to handle the possible _?whatever_ string which may be trailing our **url\_path**. Here's the solution to handle all the cases :

## blockExtensions.acl

\\.exe(\\?.\*)?$
\\.msi(\\?.\*)?$
\\.msu(\\?.\*)?$
\\.torrent(\\?.\*)?$

You will still be hated for limiting people's need to download and install shit on their Windows but you implemented it the right way and no script kiddie can brag about bypassing you ;)
