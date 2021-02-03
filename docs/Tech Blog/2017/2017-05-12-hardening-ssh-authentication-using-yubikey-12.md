---
title: "Hardening SSH authentication using Yubikey (1/2)"
date: "2017-05-12"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "security"
  - "ssh"
  - "yubikey"
---

I recently worked a bit at how we could secure better our SSH connections to our servers at work.

So far we are using the OpenSSH public key only mechanism which means that there is no password set on the servers for our users. While this was satisfactory for a time we think that this still suffers some disadvantages such as:

- we cannot enforce SSH private keys to have a passphrase on the user side
- the security level of the whole system is based on the protection of the private key which means that it's directly tied to the security level of the desktop of the users

This lead us to think about adding a 2nd factor authentication to SSH and about the usage of **security keys**.

## Meet the Yubikey

[Yubikeys](https://www.yubico.com/products/yubikey-hardware/) are security keys made by Yubico. They can support multiple modes and work with the [U2F](https://en.wikipedia.org/wiki/Universal_2nd_Factor) open authentication standard which is why they got my attention.

I decided to try the **Yubikey 4** because it can act as a smartcard while offering these interesting features:

- Challenge-Response
- OTP
- GPG
- PIV

![](images/YubiKey-4-1000-2016.png)

# Method 1 - SSH using pam\_ssh + pam\_yubico

The first method I found satisfactory was to combine **pam\_ssh** authentication module along with **pam\_yubico** as a 2nd factor. This allows server side passphrase enforcement on SSH and the usage of the security key to login.

TL;DR: two gotchas before we begin

- This method is still quite complex to setup but allows you to use the [cheaper U2F only Yubikeys](https://www.yubico.com/product/fido-u2f-security-key/).
- The [second method based on PIV](http://www.ultrabug.fr/hardening-ssh-authentication-using-yubikey-22/) is the solution we chose as it fits better our use cases and ecosystem.

> _ADVISE: keep a root SSH session to your servers while deploying/testing this so you can revert any change you make and avoid to lock yourself out of your servers._

## Setup pam\_ssh

Use **pam\_ssh on the servers** to force usage of a passphrase on a private key. The idea behind pam\_ssh is that the passphrase of your SSH key serves as your SSH password.

Generate your SSH key pair with a passphrase **on your local machine**.

ssh-keygen -f identity
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in identity.
Your public key has been saved in identity.pub.
The key fingerprint is:
SHA256:a2/HNCe28+bpMZ2dIf9bodnBwnmD7stO5sdBOV6teP8 alexys@yazd
The key's randomart image is:
+---\[RSA 2048\]----+
|                 |
|                 |
|                o|
|            . ++o|
|        S    BoOo|
|         .  B %+O|
|        o  + %+\*=|
|       . .. @ .\*+|
|         ....%B.E|
+----\[SHA256\]-----+

You then must copy your **private key** (named **identity** with no extension) **to your servers** under  the **~/.ssh/login-keys.d/** folder.

In your $HOME on the servers, you will get something like this:

.ssh/
├── known\_hosts
└── login-keys.d
    └── identity

Then you can enable the pam\_ssh authentication. Gentoo users should enable the **pam\_ssh** USE flag for **sys-auth/pambase** and re-install.

Add this **at the beginning** of the file **/etc/pam.d/ssh**

auth    required    pam\_ssh.so debug

The debug flag can be removed after you tested it correctly.

## Disable public key authentication

Because it takes precedence over the PAM authentication mechanism, you have to disable OpenSSH PubkeyAuthentication authentication on **/etc/ssh/sshd\_config:**

PubkeyAuthentication no

Enable PAM authentication on **/etc/ssh/sshd\_config**

ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM yes

## Test pam\_ssh

Now you should be prompted for your SSH passphrase to login through SSH.

➜  ~ ssh cheetah
SSH passphrase:

## Setup 2nd factor using pam\_yubico

Now we will make use of our Yubikey security key to add a 2nd factor authentication to login through SSH on our servers.

Because the Yubikey is not physically plugged on the server, we cannot use an offline Challenge-Response mechanism, so we will have to use a third party to validate the challenge. Yubico gracefully provide an API for this and the [pam\_yubico](https://github.com/Yubico/yubico-pam) module is meant to use it easily.

### Preparing your account using your Yubikey (on your machine)

First of all, you need to get your Yubico API key ID from the following URL:

- [https://upgrade.yubico.com/getapikey/](https://upgrade.yubico.com/getapikey/)
- enter your email address
- tap your Yubikey to generate an OTP in the **Yubikey OTP** field

You will get a **Client ID** (this you will use) and **Secret Key** (this you will keep safe).

**Then you will need to create an authorization mapping file** which basically link your account to a Yubikey fingerprint (modhex). This is equivalent to saying "this Yubikey belongs to this user and can authenticate him".

First, get your modhex:

- go to [https://demo.yubico.com/php-yubico/Modhex\_Calculator.php](https://demo.yubico.com/php-yubico/Modhex_Calculator.php)
- select OTP
- tap your key
- click "convert all formats"
- the modhex is listed as **Modhex encoded: xxccccxxuuxx**

Using this modhex, create your mapping file named **authorized\_yubikeys** which will be copied to **~/.yubico/authorized\_yubikeys** on the servers (replace LOGIN\_USERNAME with your actual account login name).

LOGIN\_USERNAME:xxccccxxuuxx

NOTE: this mapping file can be a centralized one (in /etc for example) to handle all the users from a server. See the the [authfile option on the doc](https://github.com/Yubico/yubico-pam#configuration).

### Setting up OpenSSH (on your servers)

**You must install pam\_yubico on the servers**. For Gentoo, it's as simple as:

emerge sys-auth/pam\_yubico

**Copy your authentication mapping file** to your home under the .yubico folder **on all servers**. You should get this:

.yubico/
└── authorized\_yubikey

Configure pam to use pam\_yubico. Add this **after the pam\_ssh** on the file **/etc/pam.d/ssh** which should look like this now:

auth    required    pam\_ssh.so
auth    required    pam\_yubico.so id=YOUR\_API\_ID debug debug\_file=/var/log/auth.log

The debug and debug\_file flags can be removed after you tested it correctly.

## Testing pam\_yubico

Now you should be prompted for your SSH passphrase and then for your Yubikey OTP to login through SSH.

➜  ~ ssh cheetah
SSH passphrase: 
YubiKey for \`ultrabug':

## About the Yubico API dependency

Careful readers will notice that using pam\_yubico introduces a strong dependency on the Yubico API availability. **If the API becomes unreachable or your internet connection goes down then your servers would be unable to authenticate you!**

The solution I found to this problem is to instruct pam to ignore the Yubikey authentication when pam\_yubico is unable to contact the API.

In this case, the module will return a AUTHINFO\_UNAVAIL code to PAM which we can act upon using the following syntax. The **/etc/pam.d/ssh** first lines should be changed to this:

auth    required    pam\_ssh.so
auth    \[success=done authinfo\_unavail=ignore new\_authtok\_reqd=done default=die\]    pam\_yubico.so id=YOUR\_API\_ID debug debug\_file=/var/log/auth.log

Now you can be sure to be able to use your Yubikey even if the API is down or unreachable ;)
