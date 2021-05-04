---
title: "Hardening SSH authentication using Yubikey (3/2)"
date: "2017-05-16"
categories:
  - "linux"
tags:
  - "gentoo"
  - "security"
  - "ssh"
  - "yubikey"
---

In my previous blog post, I demonstrated [how to use the PIV feature of a Yubikey to add a 2nd factor authentication to SSH](http://www.ultrabug.fr/hardening-ssh-authentication-using-yubikey-22/).

Careful readers such as Grzegorz Kulewski pointed out that **using the GPG capability of the Yubikey was also a great, more versatile and more secure option on the table** (I love those community insights):

- GPG keys and subkeys are indeed more flexible and can be used for case-specific operations (signing, encryption, authentication)
- GPG is more widely used and one could use their Yubikey smartcard for SSH, VPN, HTTP auth and code signing
- The Yubikey 4 GPG feature supports 4096 bit keys (limited to 2048 for PIV)

While I initially looked at the GPG feature, its apparent complexity got me to discard it for my direct use case (SSH). But I couldn't resist the good points of Grzegorz and here I got back into testing it. Thank you again Grzegorz for the excuse you provided ;)

**So let's get through with the GPG feature of the Yubikey to authenticate our SSH connections**. Just like the PIV method, this one has the  advantage to allow a 2nd factor authentication while using the public key authentication mechanism of OpenSSH and thus does not need any kind of setup on the servers.

# Method 3 - SSH using Yubikey and GPG

## Acknowledgement

The first choice you have to make is to decide whether you allow your master key to be stored on the Yubikey or not. This choice will be guided by how you plan to use and industrialize your usage of the GPG based SSH authentication.

Consider this to choose whether to store the master key on the Yubikey or not:

- (con) it will not allow the usage of the same GPG key on multiple Yubikeys
- (con) if you loose your Yubikey, you will have to revoke your entire GPG key and start from scratch (since the secret key is stored on the Yubikey)
- (pro) by storing everything on the Yubikey, you won't necessary have to have an offline copy of your master key (and all the process that comes with it)
- (pro) it is easier to generate and store everything on the key and is then a good starting point for new comers or rare GPG users

Because I want to demonstrate and enforce the most straightforward way of using it, I will base this article on generating and storing everything on a Yubikey 4. You can find useful links at the end of the article pointing to reference on how to do it differently.

## Tools installation

For this to work, we will need some tools on our local machine to setup our Yubikey correctly.

Gentoo users should install those packages:

```bash
# emerge -av dev-libs/opensc sys-auth/ykpers app-crypt/ccid sys-apps/pcsc-tools app-crypt/gnupg
```

Gentoo users should also allow the **pcscd** service to be hotplugged (started automatically upon key insertion) by modifying their **/etc/rc.conf** and having:

```
rc_hotplug="pcscd"
```

## Yubikey setup

The idea behind the Yubikey setup is to generate and store the GPG keys directly on our Yubikey and to secure them via a PIN code (and an admin PIN code).

- default PIN code: 123456
- default admin PIN code: 12345678

### USB operating mode

First, insert your Yubikey and let's change its USB operating mode to OTP+U2F+CCID with MODE_FLAG_EJECT flag.

```bash
$ ykpersonalize -m86

Firmware version 4.3.4 Touch level 783 Program sequence 3

The USB mode will be set to: 0x86

Commit? (y/n) [n]: y
```

!!! note
    If you have an older version of Yubikey (before Sept. 2014), use `-m82` instead.

### Generate a new GPG key on the Yubikey

Let's open the smartcard for edition.

```bash
$ gpg --card-edit --expert

Reader ...........: Yubico Yubikey 4 OTP U2F CCID (0005435106) 00 00
Application ID ...: A7560001240102010006054351060000
Version ..........: 2.1
Manufacturer .....: Yubico
Serial number ....: 75435106
Name of cardholder: [not set]
Language prefs ...: [not set]
Sex ..............: unspecified
URL of public key : [not set]
Login data .......: [not set]
Signature PIN ....: forced
Key attributes ...: rsa2048 rsa2048 rsa2048
Max. PIN lengths .: 127 127 127
PIN retry counter : 3 0 3
Signature counter : 0
Signature key ....: [none]
Encryption key....: [none]
Authentication key: [none]
General key info..: [none]
```

Then switch to **admin** mode.

```
gpg/card> admin
Admin commands are allowed
```

We can start generating the **Signature, Encryption and Authentication keys** on the Yubikey. During the process, you will be prompted alternatively for the **admin PIN and PIN**.

```bash
gpg/card> generate
Make off-card backup of encryption key? (Y/n)

Please note that the factory settings of the PINs are
    PIN = '123456'     Admin PIN = '12345678'
You should change them using the command --change-pin
```

!!! note
    I advise you say Yes to the off-card backup of the encryption key.

**Yubikey 4 users can choose a 4096 bits key**, let's go for it for every key type.

```
What keysize do you want for the Signature key? (2048) 4096
The card will now be re-configured to generate a key of 4096 bits
Note: There is no guarantee that the card supports the requested size.
      If the key generation does not succeed, please check the
      documentation of your card to see what sizes are allowed.

What keysize do you want for the Encryption key? (2048) 4096
The card will now be re-configured to generate a key of 4096 bits

What keysize do you want for the Authentication key? (2048) 4096
The card will now be re-configured to generate a key of 4096 bits
```

Then you're asked for the **expiration** of your key. I choose 1 year but it's up to you (leave 0 for no expiration).

```
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 1y
Key expires at mer. 15 mai 2018 21:42:42 CEST
Is this correct? (y/N) y
```

Finally you give GnuPG details about your **user ID** and you will be prompted for a **passphrase** (make it strong).

```
GnuPG needs to construct a user ID to identify your key.

Real name: Ultrabug
Email address: ultrabug@nospam.com
Comment:
You selected this USER-ID:
    "Ultrabug <ultrabug@nospam.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
```

If you chose to make an **off-card backup** of your key, you will also get notified of its location as well the **revocation certificate**.

```
gpg: Note: backup of card key saved to '/home/ultrabug/.gnupg/sk_8E407636C9C32C38.gpg'
gpg: key 22A73AED8E766F01 marked as ultimately trusted
gpg: revocation certificate stored as '/home/ultrabug/.gnupg/openpgp-revocs.d/A1580FD98C0486D94C1BE63B22A73AED8E766F01.rev'
public and secret key created and signed.
```

Make sure to **store that backup in a secure and offline location**!

You can verify that everything went good and take this chance to note the public key ID.

```
gpg/card> verify

Reader ...........: Yubico Yubikey 4 OTP U2F CCID (0001435106) 00 00
Application ID ...: A7560001240102010006054351060000
Version ..........: 2.1
Manufacturer .....: Yubico
Serial number ....: 75435106
Name of cardholder: [not set]
Language prefs ...: [not set]
Sex ..............: unspecified
URL of public key : [not set]
Login data .......: [not set]
Signature PIN ....: forced
Key attributes ...: rsa4096 rsa4096 rsa4096
Max. PIN lengths .: 127 127 127
PIN retry counter : 3 0 3
Signature counter : 4
Signature key ....: A158 0FD9 8C04 86D9 4C1B E63B 22A7 3AED 8E76 6F01
 created ....: 2017-05-16 20:43:17
Encryption key....: E1B6 7009 907D 1D94 B200 37D7 8E40 7636 C9C3 2C38
 created ....: 2017-05-16 20:43:17
Authentication key: AAED AB8E E055 41B2 EFFF 62A4 164F 873A 75D2 AD6B
 created ....: 2017-05-16 20:43:17
General key info..: pub rsa4096/22A73AED8E766F01 2017-05-16 Ultrabug <ultrabug@nospam.com>
sec> rsa4096/22A73AED8E766F01 created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106
ssb> rsa4096/164F873A75D2AD6B created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106
ssb> rsa4096/8E407636C9C32C38 created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106
```

You'll find the public key ID on the _"General key info"_ line (22A73AED8E766F01):

```
General key info..: pub rsa4096/22A73AED8E766F01 2017-05-16 Ultrabug <ultrabug@nospam.com>

Quit the card edition.

gpg/card> quit
```

It is then convenient to upload your public key to a key server, whether public or on your own web server (you can also keep it to be used and imported directly from an USB stick).

### Export the GPG public key

```bash
$ gpg --armor --export 22A73AED8E766F01 > 22A73AED8E766F01.asc
```

Then **upload it to your http server or a public server** (needed if you want to be able to easily use the key on multiple machines):

#### Upload it to your http server

```bash
$ scp 22A73AED8E766F01.asc user@server:public_html/static/22A73AED8E766F01.asc
```

#### OR upload it to a public keyserver

```bash
$ gpg --keyserver hkps://hkps.pool.sks-keyservers.net --send-key 22A73AED8E766F01
```

### Finish the Yubikey setup

Now we can finish up the Yubikey setup. Let's edit the card again:

```bash
$ gpg --card-edit --expert

Reader ...........: Yubico Yubikey 4 OTP U2F CCID (0001435106) 00 00
Application ID ...: A7560001240102010006054351060000
Version ..........: 2.1
Manufacturer .....: Yubico
Serial number ....: 75435106
Name of cardholder: [not set]
Language prefs ...: [not set]
Sex ..............: unspecified
URL of public key : [not set]
Login data .......: [not set]
Signature PIN ....: forced
Key attributes ...: rsa4096 rsa4096 rsa4096
Max. PIN lengths .: 127 127 127
PIN retry counter : 3 0 3
Signature counter : 4
Signature key ....: A158 0FD9 8C04 86D9 4C1B E63B 22A7 3AED 8E76 6F01
 created ....: 2017-05-16 20:43:17
Encryption key....: E1B6 7009 907D 1D94 B200 37D7 8E40 7636 C9C3 2C38
 created ....: 2017-05-16 20:43:17
Authentication key: AAED AB8E E055 41B2 EFFF 62A4 164F 873A 75D2 AD6B
 created ....: 2017-05-16 20:43:17
General key info..: pub rsa4096/22A73AED8E766F01 2017-05-16 Ultrabug <ultrabug@nospam.com>
sec> rsa4096/22A73AED8E766F01 created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106
ssb> rsa4096/164F873A75D2AD6B created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106
ssb> rsa4096/8E407636C9C32C38 created: 2017-05-16 expires: 2018-05-16
 card-no: 0001 05435106

gpg/card> admin
```

**Make sure that the Signature PIN is forced** to request that your PIN is entered when your key is used. **If it is listed as "not forced"**, you can enforce it by entering the following command:

```
gpg/card> forcesig
```

It is also good practice to set a few more settings on your key.

```
gpg/card> login
Login data (account name): ultrabug

gpg/card> lang
Language preferences: en

gpg/card> name
Cardholder's surname: Bug
Cardholder's given name: Ultra
```

Now we need to **setup the PIN and admin PIN on the card**.

```
gpg/card> passwd
gpg: OpenPGP card no. A7560001240102010006054351060000 detected

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? 1
PIN changed.

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? 3
PIN changed.

1 - change PIN
2 - unblock PIN
3 - change Admin PIN
4 - set the Reset Code
Q - quit

Your selection? Q
```

If you uploaded your public key on your web server or a public server, configure it on the key:

```
gpg/card> url
URL to retrieve public key: http://ultrabug.fr/keyserver/22A73AED8E766F01.asc

gpg/card> quit
```

Now we can quit the gpg card edition, we're done on the Yubikey side!

```
gpg/card> quit
```

## SSH client setup

This is the setup on the machine(s) where you will be using the GPG key.
The idea is to import your key from the card to your local keyring so you can
use it on gpg-agent (and its ssh support).

You can skip the fetch/import part below if you generated the key on the same
machine than you are using it. You should see it listed when executing _gpg -k_.

Plug-in your Yubikey and load the smartcard.

```bash
$ gpg --card-edit --expert
```

Then fetch the key from the URL to import it to your local keyring.

```
gpg/card> fetch
```

Then you're done on this part, exit gpg and update/display& your card status.

```
gpg/card> quit
```

```bash
$ gpg --card-status
```

You can verify the presence of the key in your keyring:

```bash
$ gpg -K
sec>  rsa4096 2017-05-16 [SC] [expires: 2018-05-16]
      A1580FD98C0486D94C1BE63B22A73AED8E766F01
      Card serial no. = 0001 05435106
uid           [ultimate] Ultrabug <ultrabug@nospam.com>
ssb>  rsa4096 2017-05-16 [A] [expires: 2018-05-16]
ssb>  rsa4096 2017-05-16 [E] [expires: 2018-05-16]
```

!!! note
    The "Card serial no." showing that the key is actually stored on a smartcard.

Now we need to **configure gpg-agent to enable ssh support**, edit your **~/.gnupg/gpg-agent.conf** configuration file and make sure that the **_enable-ssh-support_** is present:

```
default-cache-ttl 7200
max-cache-ttl 86400
enable-ssh-support
```

Then you will need to update your **~/.bashrc** file to automatically start gpg-agent and override ssh-agent's environment variables. Add this at the end of your **~/.bashrc** file (or equivalent).

```
# start gpg-agent if it's not running
# then override SSH authentication socket to use gpg-agent
pgrep -l gpg-agent &>/dev/null
if [[ "$?" != "0" ]]; then
 gpg-agent --daemon &>/dev/null
fi
SSH_AUTH_SOCK=/run/user/$(id -u)/gnupg/S.gpg-agent.ssh
export SSH_AUTH_SOCK
```

To simulate a clean slate, unplug your card then kill any running gpg-agent:

```bash
$ killall gpg-agent
```

Then **plug back your card and source your ~/.bashrc** file:

```bash
$ source ~/.bashrc
```

Your GPG key is now listed in you ssh identities!

```bash
$ ssh-add -l
4096 SHA256:a4vsJM6Sw1Rt8orvPnI8nvNUwHbRQ67ylnoTxruozK9 cardno:000105435106 (RSA)
```

You will now be able to **get the SSH public key hash to copy to your remote servers** using:

```bash
$ ssh-add -L
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCVDq24Ld/bOzc3yNnY6fF7FNfZnb6wRVdN2xMo1YiA5pz20y+2P1ynq0rb6l/wsSip0Owq4G6fzaJtT1pBUAkEJbuMvZBrbYokb2mZ78iFZyzAkCT+C9YQtvPClFxSnqSL38jBpunZuuiFfejM842dWdMNK3BTcjeTQdTbmY+VsVOw7ppepRh7BWslb52cVpg+bHhB/4H0BUUd/KHZ5sor0z6e1OkqIV8UTiLY2laCCL8iWepZcE6n7MH9KItqzX2I9HVIuLCzhIib35IRp6d3Whhw3hXlit4/irqkIw0g7s9jC8OwybEqXiaeQbmosLromY3X6H8++uLnk7eg9RtCwcWfDq0Qg2uNTEarVGgQ1HXFr8WsjWBIneC8iG09idnwZNbfV3ocY5+l1REZZDobo2BbhSZiS7hKRxzoSiwRvlWh9GuIv8RNCDss9yNFxNUiEIi7lyskSgQl3J8znDXHfNiOAA2X5kVH0s6AQx4hQP9Dl1X2Em4zOz+yJEPFnAvE+XvBys1yuUPq1c3WKMWzongZi8JNu51Yfj7Trm74hoFRn+CREUNpELD9JignxlvkoKAJpWVLdEu1bxJ7jh7kcMQfVEflLbfkEPLV4nZS4sC1FJR88DZwQvOudyS69wLrF3azC1Gc/fTgBiXVVQwuAXE7vozZk+K4hdrGq4u7Gw== cardno:000105435106
```

_This is what ends up in ~/.ssh/authorized_keys on your servers._

**When connecting to your remote server, you will be prompted for the PIN!**

## Conclusion

Using the GPG feature of your Yubikey is very convenient and versatile. Even if it is not that hard after all, it is interesting and fair to note that the PIV method is indeed more simple to implement.

When you need to maintain a large number of security keys in an organization and that their usage is limited to SSH, you will be inclined to stick with PIV if 2048 bits keys are acceptable for you.

However, for power users and developers, usage of GPG is definitely something you need to consider for its versatility and enhanced security.

## Useful links

You may find those articles useful to setup your GPG key differently and avoid having the secret key tied to your Yubikey.

- [https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-openpgp/#generatelocal](https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-openpgp/#generatelocal)
- [https://www.esev.com/blog/post/2015-01-pgp-ssh-key-on-yubikey-neo/](https://www.esev.com/blog/post/2015-01-pgp-ssh-key-on-yubikey-neo/)
- [https://www.jfry.me/articles/2015/gpg-smartcard/](https://www.jfry.me/articles/2015/gpg-smartcard/)
