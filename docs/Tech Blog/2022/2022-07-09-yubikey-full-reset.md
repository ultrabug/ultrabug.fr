---
title: "How to reset your Yubikey when you locked your PIN"
date: "2022-07-09"
categories:
  - "linux"
tags:
  - "yubikey"
  - "security"
  - "gpg"
  - "ssh"
---

# How to reset your Yubikey when you locked your PIN

This article is a short reminder of the procedure to follow to reset a Yubikey
to its factory defaults and thus reset the user and admin PIN when you locked
them after too many unsuccessful tries using GPG/SSH.

```bash
gpg --card-status
Application ID ...: D2760001240102010006090289860000
Version ..........: 2.1
Manufacturer .....: Yubico
Serial number ....: 09992652
Name of cardholder: [not set]
Language prefs ...: [not set]
Sex ..............: unspecified
URL of public key : [not set]
Login data .......: [not set]
Signature PIN ....: not forced
Key attributes ...: 2048R 2048R 2048R
Max. PIN lengths .: 127 127 127
PIN retry counter : 0 0 3
Signature counter : 0
Signature key ....: [none]
Encryption key....: [none]
Authentication key: [none]
General key info..: [none]
```

This procedure should be used only if you don't have a PUK code to use, which
is the simple and non-destructive way to recover from a locked PIN situation.

## Using a PUK code (non-destructive)

Using a PUK code, you can use the `passwd` command in gpg to clear the PIN
lock counters.

```bash
$ gpg --card-edit --expert

gpg/card> help
quit           quit this menu
admin          show admin commands
help           show this help
list           list all available data
fetch          fetch the key specified in the card URL
passwd         menu to change or unblock the PIN
verify         verify the PIN and list all data
unblock        unblock the PIN using a Reset Code

gpg/card> passwd
gpg: OpenPGP card no. XXXXXXXXXXXXXXXXXX detected

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? 2
```

## Reset your Yubikey to factory defaults (destructive)

So you locked your GPG (user/admin) PIN counters?

```
PIN retry counter : 0 0 3
                    ^   ^
     user PIN counter   admin PIN counter
```

!!! warning
    Reseting your Yubikey to its factory defaults means that you will loose
    everything stored on it, so you'll have to setup your GPG/SSH again!

The [procedure](https://forum.yubico.com/viewtopicfcb3.html?p=8245#p8245) is
about sending hexadecimal commands through the gpg-agent:

```bash
$ gpg-connect-agent --hex

> scd apdu 00 20 00 81 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 81 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 81 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 81 08 40 40 40 40 40 40 40 40
D[0000] 69 83 i.
OK
> scd apdu 00 20 00 83 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 83 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 83 08 40 40 40 40 40 40 40 40
D[0000] 69 82 i.
OK
> scd apdu 00 20 00 83 08 40 40 40 40 40 40 40 40
D[0000] 69 83 i.
OK
> scd apdu 00 e6 00 00
D[0000] 90 00 ..
OK
> scd apdu 00 44 00 00
D[0000] 90 00 ..
OK
>
```

Then unplug/replug your Yubikey + restart your gpg-agent daemon:

```bash
$ pkill gpg-agent && pkill scdaemon
$ gpg-agent --card-status

[...]
PIN retry counter : 3 0 3
[...]
```

