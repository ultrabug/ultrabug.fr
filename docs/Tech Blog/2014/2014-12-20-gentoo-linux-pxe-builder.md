---
title: "Gentoo Linux PXE builder"
date: "2014-12-20"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "pxe"
---

Due to a bad hardware failure a few weeks ago at work, I had to rebuild a good part of our PXE stack and I ended up once again looking for the steps to **build a PXE-ready Gentoo initramfs**.

Then I realized that, while I was at it, I wanted this PXE initramfs to feature more than a Live CD like boot because I use PXE to actually install my servers automatically using ansible. So why not embed all my needs straight into the PXE initramfs and automate the whole boring creation process of it ?

That what the [gentoo-pxe-builder](https://github.com/ultrabug/gentoo-pxe-builder) project is about and I thought I'd open source it in case it could help and spare some time to anyone else.

The main idea is to provide a simple bash script which bases itself on the latest Gentoo liveCD kernel/initramfs to prepare a PXE suitable version which you can easily hack into without having to handle all the squashfs/cpio hassle to rebuild it.

Quick steps it does for you :

- download the latest live CD
- extract the kernel / initramfs from it
- **patch** the embedded squashfs to make it PXE ready
- **setup SSH and a default root password** so you can connect to your PXE booted machine directly
- add a **hackable local.d start script** which will be executed at the end of the PXE boot

The provided local.d start script provides IP address display so you can actually see the IP address being setup on your PXE host and it will also display the **real name of the network interfaces detected on the host based on udev deterministic naming**.

You can read everything in [more details on the project's README](https://github.com/ultrabug/gentoo-pxe-builder/blob/master/README.md).

Of course it's mainly oriented to my use case and I'm sure the process / patching could be even more elegant so anyone feel free to contribute or ask/propose some features, I'll happily follow them up !
