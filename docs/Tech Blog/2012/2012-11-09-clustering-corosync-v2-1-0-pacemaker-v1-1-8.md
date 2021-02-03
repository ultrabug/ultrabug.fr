---
title: "Clustering : corosync v2.1.0 & pacemaker v1.1.8"
date: "2012-11-09"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "portage"
---

I recently bumped quite a bunch of the clustering suite packages such as :

- sys-cluster/cluster-glue-1.0.11
- sys-cluster/libqb-0.14.3
- sys-cluster/corosync-1.4.4
- sys-cluster/corosync-2.1.0
- sys-cluster/crmsh-1.2.1 (new package)

## corosync-2.1.0

You should be aware that the corosync-2.x packages are still hard masked because the 2.0.x ones didn't compile properly and we didn't have a suitable pacemaker version for it to work with.

There is another thing for us to consider and handle in the ebuilds when we'll be willing to release **corosync-2 : it is not backward compatible** ! So yes, you will either have to start with a fresh cluster or break your existing ones to migrate to corosync-2. The reason is that upstream decided to drop the plugins support from their software. So a non-plugin cluster cannot work with a plugin-enabled one.

## pacemaker-1.1.8

As for pacemaker-1.1.8, [the bump request](https://bugs.gentoo.org/show_bug.cgi?id=439762) took quite some time. The reason is that it was released **without backward compatibility** support as well so you couldn't join your existing pacemaker-1.1.x cluster even when using corosync-1.x ! I found it unacceptable because this meant I would have to force for corosync-2 usage starting from pacemaker-1.1.8 for no real reason. Pacemaker upstream, namely [Andrew Beekhof](http://theclusterguy.clusterlabs.org/), is very responsive and kind so [he offered a solution](http://bugs.clusterlabs.org/show_bug.cgi?id=5114) which I'm happy to provide to Gentoo users.

## crmsh-1.2.1

The **crm** command is not included in the pacemaker sources anymore. It is now an [independent project](https://savannah.nongnu.org/projects/crmsh/) lead by Dejan Muhamedagic to allow more versatility in its development and a better iteration of releases. I packaged and released it along with pacemaker-1.1.8 as well.

## Todo

I'm still slacking on the sys-cluster/resource-agents package unfortunately. I already discussed with upstream about it as it's not a straightforward bump because they merged two different resource-agents developments. I think to have a pretty good idea of what needs to be done and will do my best to fix this gap as soon as I can.
