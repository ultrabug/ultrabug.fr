---
title: "Gentoo Linux on DELL XPS 13 9365 and 9360"
date: "2017-11-02"
categories: 
  - "linux"
tags: 
  - "9360"
  - "9365"
  - "dell"
  - "gentoo"
  - "uefi"
  - "xps"
---

Since I received some positive feedback about my previous [DELL XPS 9350 post](http://www.ultrabug.fr/gentoo-linux-on-dell-xps-13-9350/), I am writing this summary about my recent experience in installing **Gentoo Linux on a DELL XPS 13 9365**.

This installation notes goals:

- UEFI boot using Grub
- Provide you with a complete and working kernel configuration
- Encrypted disk root partition using LUKS
- Be able to type your LUKS passphrase to decrypt your partition using your local keyboard layout

## Grub & UEFI & Luks installation

This installation is a fully UEFI one using grub and booting an encrypted root partition (and home partition). I was happy to see that since my previous post, everything got smoother. So even if you can have this installation working using MBR, I don't really see a point in avoiding UEFI now.

## BIOS configuration

Just like with its ancestor, you should:

- **Turn off Secure Boot**
- Set **SATA Operation** to **AHCI**

## Live CD

Once again, go for the latest SystemRescueCD (it’s Gentoo based, you won’t be lost) as it’s quite more up to date and supports booting on UEFI. Make it a Live USB for example using **unetbootin** and the **ISO** on a **vfat formatted USB stick**.

## NVME SSD disk partitioning

We’ll obviously use **GPT with UEFI**. I found that using **gdisk** was the easiest. The disk itself is found on **/dev/nvme0n1**. Here it is the partition table I used :

- 10Mo UEFI BIOS partition (type EF02)
- 500Mo UEFI boot partition (type EF00)
- 2Go Swap partition
- 475Go Linux root partition

The corresponding gdisk commands :

\# gdisk /dev/nvme0n1

Command: o ↵
This option deletes all partitions and creates a new protective MBR.
Proceed? (Y/N): y ↵

Command: n ↵
Partition Number: 1 ↵
First sector: ↵
Last sector: +10M ↵
Hex Code: EF02 ↵

Command: n ↵
Partition Number: 2 ↵
First sector: ↵
Last sector: +500M ↵
Hex Code: EF00 ↵

Command: n ↵
Partition Number: 3 ↵
First sector: ↵
Last sector: +2G ↵
Hex Code: 8200 ↵

Command: n ↵
Partition Number: 4 ↵
First sector: ↵
Last sector: ↵ (for rest of disk)
Hex Code: ↵

Command: p ↵
Disk /dev/nvme0n1: 1000215216 sectors, 476.9 GiB
Logical sector size: 512 bytes
Disk identifier (GUID): A73970B7-FF37-4BA7-92BE-2EADE6DDB66E
Partition table holds up to 128 entries
First usable sector is 34, last usable sector is 1000215182
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048           22527   10.0 MiB    EF02  BIOS boot partition
   2           22528         1046527   500.0 MiB   EF00  EFI System
   3         1046528         5240831   2.0 GiB     8200  Linux swap
   4         5240832      1000215182   474.4 GiB   8300  Linux filesystem

Command: w ↵
Do you want to proceed? (Y/N): Y ↵

## No WiFi on Live CD ? no panic

Once again on my (old?) SystemRescueCD stick, the integrated Intel 8265/8275 wifi card is not detected.

So I used my old trick with my Android phone connected to my local WiFi as a USB modem which was detected directly by the live CD.

- get your Android phone connected on your local WiFi (unless you want to use your cellular data)
- plug in your phone using USB to your XPS
- on your phone, go to Settings / More / Tethering & portable hotspot
- enable **USB tethering**

Running **ip addr** will show the network card **enp0s20f0u2** (for me at least), then if no IP address is set on the card, just ask for one :

\# dhcpcd enp0s20f0u2

You have now access to the internet.

## Proceed with installation

The only thing to prepare is to format the UEFI boot partition as FAT32. Do not worry about the UEFI BIOS partition (/dev/nvme0n1p1), grub will take care of it later.

\# mkfs.vfat -F 32 /dev/nvme0n1p2

**Do not forget to use cryptsetup to encrypt your /dev/nvme0n1p4 partition!** In the rest of the article, I'll be using its device mapper representation.

\# cryptsetup luksFormat -s 512 /dev/nvme0n1p4
# cryptsetup luksOpen /dev/nvme0n1p4 root
# mkfs.ext4 /dev/mapper/root

**Then follow the Gentoo handbook** as usual for the stage3 related next steps. **Make sure you mount and bind the following to your /mnt/gentoo LiveCD installation folder** (the /sys binding is important for grub UEFI):

\# mount -t proc none /mnt/gentoo/proc
# mount -o bind /dev /mnt/gentoo/dev
# mount -o bind /sys /mnt/gentoo/sys

## make.conf settings

I strongly recommend using at least the following on your **/etc/portage/make.conf** :

GRUB_PLATFORM="efi-64"
INPUT_DEVICES="evdev synaptics"
VIDEO_CARDS="intel i965"

USE="bindist cryptsetup"

The **GRUB_PLATFORM** one is important for later grub setup and the **cryptsetup** USE flag will help you along the way.

## fstab for SSD

Don't forget to make sure the **noatime** option is used on your fstab for / and /home.

/dev/nvme0n1p2    /boot    vfat    noauto,noatime    1 2
/dev/nvme0n1p3    none     swap    sw                0 0
/dev/mapper/root  /        ext4    noatime   0 1

## Kernel configuration and compilation

I suggest you use a recent **\>=sys-kernel/gentoo-sources-4.13.0** along with **genkernel**.

- You can [download my kernel configuration file](http://ultrabug.fr/gentoo/xps9365/kernel-config-x86_64-4.13.10-gentoo) (iptables, docker, luks & stuff included)
- Put the kernel configuration file into the **/etc/kernels/** directory (with a training s)
- Rename the configuration file with the exact version of your kernel

Then you'll need to configure genkernel to add luks support, firmware files support and keymap support if your keyboard layout is not QWERTY.

In your **/etc/genkernel.conf**, change the following options:

LUKS="yes"
FIRMWARE="yes"
KEYMAP="1"

Then run **genkernel all** to build your kernel and luks+firmware+keymap aware initramfs.

## Grub UEFI bootloader with LUKS and custom keymap support

Now it's time for the grub magic to happen so you can boot your wonderful Gentoo installation using UEFI and type your password using your favourite keyboard layout.

- make sure your boot vfat partition is mounted on /boot
- edit your **/etc/default/grub** configuration file with the following:

GRUB_CMDLINE_LINUX="crypt_root=/dev/nvme0n1p4 keymap=fr"

This will allow your initramfs to know it has to read the encrypted root partition from the given partition and to prompt for its password in the given keyboard layout (french here).

Now let's install the grub UEFI boot files and setup the UEFI BIOS partition.

\# grub-install --efi-directory=/boot --target=x86_64-efi /dev/nvme0n1
Installing for x86_64-efi platform.
Installation finished. No error reported

It should report no error, then we can generate the grub boot config:

\# grub-mkconfig -o /boot/grub/grub.cfg

You're all set!

You will get a **gentoo** UEFI boot option, you can disable the Microsoft Windows one from your BIOS to get straight to the point.

Hope this helped!
