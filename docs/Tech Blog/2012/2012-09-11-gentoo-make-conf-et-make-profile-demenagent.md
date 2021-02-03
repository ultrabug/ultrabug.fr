---
title: "Gentoo : make.conf et make.profile déménagent"
date: "2012-09-11"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
---

Bien que cette nouvelle soit diffusée par le système de news interne à Portage, je sais d'expérience qu'elles ne sont pas très lues.

Sachez simplement que prochainement, **les fichiers make.conf et make.profile seront présents dans les stages d'installation dans /etc/portage** et non plus dans /etc comme actuellement.

Il est important de noter que **ce changement ne concerne que les nouvelles installations** et n'a aucun impact sur les systèmes actuels, les deux répertoires sont donc supportés mais ne vous étonnez pas si vous ne les trouvez pas à leur place habituelle lors de vos prochaines installs. Pour ceux qui utilisent des scripts automatisés d'installation ou des démons comme Puppet ou Chef, pensez à modifier vos configurations !

La news en question, en anglais :

 

  Title                     make.conf and make.profile move
  Author                    Jorge Manuel B. S. Vicetto <jmbsvicetto@gentoo.org>
  Posted                    2012-09-09
  Revision                  1

Starting next week, new stages will have make.conf and make.profile
moved from /etc to /etc/portage. This is a change in the installation
defaults, that will only affect new installs so it doesn't affect
current systems.

Current users don't need to do anything. But if you want to follow the
preferred location, you may want to take the chance to move the files
in your system(s) to the new location.
