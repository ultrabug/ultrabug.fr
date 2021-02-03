---
title: "rabbitMQ 2.8.6 released"
date: "2012-09-03"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
  - "rabbitmq"
  - "release"
---

![](images/rabbitmq_logo_strap.png "RabbitMQ Logo")

I was in a **bug killing spree** today and I'm pleased to announce that I closed the 5 open bugs open for net-misc/rabbitmq-server while bumping this package to its new v2.8.6 version.

+\*rabbitmq-server-2.8.6 (03 Sep 2012)
+
+  03 Sep 2012; Ultrabug <ultrabug@gentoo.org> -rabbitmq-server-2.8.1-r1.ebuild,
+  rabbitmq-server-2.8.4.ebuild, rabbitmq-server-2.8.5.ebuild,
+  +rabbitmq-server-2.8.6.ebuild, files/rabbitmq.service,
+  files/rabbitmq-script-wrapper:
+  Drop old. Add GPL-2 LICENSE fix #426092. Enhanced systemd service file fix
+  #419531 and init script fix #416345 thx to Maksim Melnikau. Fix #430510 VCS
+  fetching in compilation. Fix #430508 parallel building. Version bump.
+

Bug fix version mates, the [changelog](http://lists.rabbitmq.com/pipermail/rabbitmq-announce/attachments/20120822/21528820/attachment.txt) is here for more details as always.
