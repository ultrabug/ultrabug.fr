---
title: "Tuning pacemaker for large clusters"
date: "2014-01-10"
categories: 
  - "linux"
tags: 
  - "clus"
  - "cluster"
  - "gentoo"
  - "pacemaker"
---

We've been running quite a lot of production clusters using pacemaker/corosync for a while. Some of them are large, handling **more than 200 resources** across multiple nodes and we've exceeded some limits on pacemaker's CIB size.

I thought I'd share how to tune your cluster to handle such a bunch of resources since there are some default limits on the IPC buffer size which can lead to problems when your resources (and thus CIB) grows too much.

## Hitting the IPC limit

When running a large cluster you may hit the following problem :

error: crm\_ipc\_prepare: Could not compress the message into less than the configured ipc limit (51200 bytes).Set PCMK\_ipc\_buffer to a higher value (2071644 bytes suggested)

## Evaluating the buffer size

Have a look at the size of your current CIB :

\# cibadmin -Ql > cib.xml
# ls -l cib.xml
# bzip2 cib.xml
# ls -l cib.xml.bz2

The CIB is compressed on the wire using bzip2 so you have to **compare the compressed cib.xml.bz2 with the IPC default buffer size of 51200** and you'll find the sufficient PCMK\_ipc\_buffer value for you (take more just to be safe).

## Setting the environment variables

On Gentoo Linux, you'll have to create the **/etc/env.d/90pacemaker** file containing :

PCMK\_ipc\_type=shared-mem
PCMK\_ipc\_buffer=2071644

- **PCMK\_ipc\_buffer** : you may need to increase this depending on your cluster size and needs
- **PCMK\_ipc\_type** : the shared-mem one is the default now, other values are socket|posix|sysv

You will also need to set these env. vars in your **.bashrc** so that the crm CLI doesn't break :

export PCMK\_ipc\_type=shared-mem
export PCMK\_ipc\_buffer=2071644

## Future

Finally, I wanted to let you know that the upcoming Pacemaker v1.1.11 should come with a feature which will allow the IPC layer to adjust the PCMK\_ipc\_buffer automagically !

Hopefully you shouldn't need this blog post anymore pretty soon :)

## EDIT, Jan 16 2014

Following this blog post, I had a very interesting comment from @**beekhof** (lead dev of pacemaker)

beekhof> Ultrabug: regarding large clusters, the cib in 1.1.12 will be O(2) faster than 1.1.11.
Ultrabug> beekhof: that's great news mate ! when is it scheduled to be released ?
beekhof> 30th of Feb
