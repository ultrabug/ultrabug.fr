---
title: "Consul on Gentoo Linux"
date: "2014-06-04"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "consul"
  - "gentoo"
  - "portage"
---

As a clustering and distributed architecture enthusiast, I'm naturally interested in software providing neat ways to coordinate any kind of state/configuration/you-name-it over a large number of machines.

My quest, as many of you I guess, were so far limited to tools like [zookeeper](http://zookeeper.apache.org/) ([packaged on my overlay](http://git.overlays.gentoo.org/gitweb/?p=dev/ultrabug.git;a=tree;f=sys-cluster/zookeeper) but with [almost no echo](https://bugs.gentoo.org/show_bug.cgi?id=318029)) and [doozerd](https://github.com/ha/doozerd) (last commit nearly 6 months ago) which both cover some of the goals listed above with more or less flavors and elegance (sorry guys, JAVA is NOT elegant to me).

I recently heard about **[consul](http://www.consul.io)**, a new attempt to solve some of those problems in an interesting way while providing some rich fuctionnalities so I went on giving it a try and naturally started packaging it so others can too.

## WTF is consul ?

Consul is a few months' old project (_and already available on Gentoo !_) from [the guys making Vagrant](http://www.hashicorp.com/). I especially like its datacenter centric architecture, intuitive deployment and its DNS + HTTP API query mechanisms. This sounds promising so far !

This is a descripion taken from the Hashicorp's blog :

Consul is a solution for service discovery and configuration. Consul is completely distributed, highly available, and scales to thousands of nodes and services across multiple datacenters.

Some concrete problems Consul solves: finding the services applications need (database, queue, mail server, etc.), configuring services with key/value information such as enabling maintenance mode for a web application, and health checking services so that unhealthy services aren’t used. These are just a handful of important problems Consul addresses.

Consul solves the problem of service discovery and configuration. Built on top of a foundation of rigorous academic research, Consul keeps your data safe and works with the largest of infrastructures. Consul embraces modern practices and is friendly to existing DevOps tooling.

## app-admin/consul ?

This is a RFC and interest call about the packaging and availability of **consul** for Gentoo Linux.

The latest version and live ebuilds [are present in my overlay](http://git.overlays.gentoo.org/gitweb/?p=dev/ultrabug.git;a=tree;f=app-admin/consul) so if you are interested, please tell me (here, IRC, email, whatever) and I'll consider adding it to the portage tree.

## I want to test it !

Now that would be helpful to get some feedback about the usability of the current packaging. So far the ebuild features what I think should cover a lot of use cases :

- full build from sources
- customizable consul agent init script with reload, telemetry and graceful stop support
- web UI built from sources and installation for easy deployment

\# layman -a ultrabug
# emerge -av consul

Hope this interests some of you folks !
