---
title: "Hardening SSH authentication using Yubikey (2/2)"
date: "2017-05-12"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "security"
  - "ssh"
  - "yubikey"
---

In my previous blog post, I demonstrated [how to use a Yubikey to add a 2nd factor (2FA) authentication to SSH using pam\_ssh and pam\_yubico](http://www.ultrabug.fr/hardening-ssh-authentication-using-yubikey-12/).

In this article, I will go further and demonstrate another method using **Yubikey's Personal Identity Verification (PIV) capability**.

This one has the huge advantage to allow a 2nd factor authentication while using the public key authentication mechanism of OpenSSH and thus does not need any kind of setup on the servers.

# Method 2 - SSH using Yubikey and PIV

Yubikey 4 and NEO also act as smartcards supporting the [PIV standard](https://developers.yubico.com/PIV/) which allows you to store a private key on your security key through PKCS#11. This is an amazing feature which is also very good for our use case.

## Tools installation

For this to work, we will need some tools on our local machines to setup our Yubikey correctly.

Gentoo users should install those packages:

emerge dev-libs/opensc sys-auth/ykpers sys-auth/yubico-piv-tool sys-apps/pcsc-lite app-crypt/ccid sys-apps/pcsc-tools sys-auth/yubikey-personalization-gui

Gentoo users should also allow the **pcscd** service to be hotplugged (started automatically upon key insertion) by modifying their **/etc/rc.conf** and having:

rc\_hotplug="pcscd"

## Yubikey setup

The idea behind the Yubikey setup is to generate and store a private key in our Yubikey and to secure it via a PIN code.

First, insert your Yubikey and let's change its USB operating mode to OTP+CCID.

ykpersonalize -m2
Firmware version 4.3.4 Touch level 783 Program sequence 3

The USB mode will be set to: 0x2

Commit? (y/n) \[n\]: y

Then, we will create a new management key:

key=\`dd if=/dev/random bs=1 count=24 2>/dev/null | hexdump -v -e '/1 "%02X"'\`
echo $key
D59E46FE263DDC052A409C68EB71941D8DD0C5915B7C143A

Replace the default management key (if prompted, copy/paste the key printed above):

yubico-piv-tool -a set-mgm-key -n $key --key 010203040506070801020304050607080102030405060708

Then change the default PIN code and PUK code of your Yubikey

yubico-piv-tool -a change-pin -P 123456 -N <NEW PIN>

yubico-piv-tool -a change-puk -P 12345678 -N <NEW PUK>

Now that your Yubikey is secure, let's proceed with the PCKS#11 certificate generation. You will be prompted for your management key that you generated before.

yubico-piv-tool -s 9a -a generate -o public.pem -k

Then create a self-signed certificate (only used for libpcks11) and import it in the Yubikey:

yubico-piv-tool -a verify-pin -a selfsign-certificate -s 9a -S "/CN=SSH key/" -i public.pem -o cert.pem
yubico-piv-tool -a import-certificate -s 9a -i cert.pem

Here you are! You can now export your public key to use with OpenSSH:

ssh-keygen -D opensc-pkcs11.so -e
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCWtqI37jwxYMJ9XLq9VwHgJlhZViPVAGIUfMm8SAlfs6cka4Cj570lkoGK04r8JAVJFy/iKfhGpL9N9XuartfIoq6Cg/6Qvg3REupuqs51V2cBaC/gnWIQ7qZqlzBulvcOvzNfHFD/lX42J58+E8tWnYg6GzIsImFZQVpmI6SxNfSmVQIqxIufInrbQaI+pKXntdTQC9wyNK5FAA8TXAdff5ZDnmetsOTVble9Ia5m6gqM7MnxNZ56uDpn+6lCxRZSW+Ln2PDE7sivVcST4qpfwY4P4Lrb3vrjCGODFg4xmGNKXsLi2+uZbs5rW7bg4HFO50kKDucPV1M+rBWA9999

**Copy to your servers** your SSH public key to your usual **~/.ssh/authorized\_keys** file in your $HOME.

## Testing PIV secured SSH

Plug-in your Yubikey, and then SSH to your remote server using the opensc-pkcs11 library. You will be prompted for your PIN and then successfully logged in :)

ssh -I opensc-pkcs11.so cheetah
Enter PIN for 'PIV\_II (PIV Card Holder pin)':

You can then configure SSH to use it by default for all your hosts in your **~/.ssh/config**

Host=\*
PKCS11Provider /usr/lib/opensc-pkcs11.so

## Using PIV with ssh-agent

You can also use ssh-agent to avoid typing your PIN every time.

When asked for the passphrase, enter your PIN:

ssh-add -s /usr/lib/opensc-pkcs11.so
Enter passphrase for PKCS#11: 
Card added: /usr/lib/opensc-pkcs11.so

You can verify that it worked by listing the available keys in your ssh agent:

ssh-add -L
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCWtqI37jwxYMJ9XLq9VwHgJlhZViPVAGIUfMm8SAlfs6cka4Cj570lkoGK04r8JAVJFy/iKfhGpL9N9XuartfIoq6Cg/6Qvg3REupuqs51V2cBaC/gnWIQ7qZqlzBulvcOvzNfHFD/lX42J58+E8tWnYg6GzIsImFZQVpmI6SxNfSmVQIqxIufInrbQaI+pKXntdTQC9wyNK5FAA8TXAdff5ZDnmetsOTVble9Ia5m6gqM7MnxNZ56uDpn+6lCxRZSW+Ln2PDE7sivVcST4qpfwY4P4Lrb3vrjCGODFg4xmGNKXsLi2+uZbs5rW7bg4HFO50kKDucPV1M+rBWA9999 /usr/lib64/opensc-pkcs11.so

## Enjoy!

Now you have a flexible yet robust way to authenticate your users which you can also extend by adding another type of authentication on your servers using PAM.
