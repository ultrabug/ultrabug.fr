---
title: "Clustering : resource-agents v3.9.5 & crmsh v1.2.5"
date: "2013-02-15"
categories: 
  - "linux"
tags: 
  - "cluster"
  - "gentoo"
  - "portage"
  - "release"
---

Quick post about two bumps I made yesterday. The important one is **sys-cluster/resource-agents-3.9.5** because the previous release contained a **regression on the IPaddr2 resource**. IPaddr2 didn't send unsolicited ARPs on start, depending on the ARP cache timeout time of the hosts on your topology, this could cause some serious delay when a failover takes place ! Also note the nice additions on crmsh which will make our lives easier.

## resource-agents-3.9.5

- fix IPaddr2 ARP regression
- pgsql: support starting as Hot Standby
- support for RA tracing

## crmsh-1.2.5

- cibconfig: modgroup command
- cibconfig: directed graph support
- history: diff command (between PE inputs)
- history: show command (show configuration of PE inputs)
- history: graph command
