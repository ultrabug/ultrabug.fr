---
title: "Portage basics"
date: "2012-01-11"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "portage"
---

Les distributions Linux disposent toutes de ce qu'on appelle un gestionnaire de paquet dit _package management system_ ou plus simplement _**package manager**._

- Un **_package manager_** est un ensemble de programmes et d'outils permettant l'automatisation de l'installation / mise à jour / configuration / désinstallation de logiciels sur un système.

Sous Gentoo Linux, le gestionnaire de paquet s'appelle **portage**. Il permet de manipuler les **packages** disponible sur notre système Gentoo.

- Un **_package_** représente un logiciel disponible à travers le package manager. Selon les distributions il peut prendre différentes formes comme par exemple une archive compressée.

# Portage

Portage est écrit en **python** et en **bash**. C'est sans conteste l'un des package manager les plus flexibles et performants car il offre des possibilités de personnalisation très fines des packages que l'on souhaite installer sur son système.

La liste des packages disponibles à l'installation est organisée dans une arborescence de dossiers, c'est ce qu'on appelle le **portage tree**. Le nom "arbre portage" fait référence à l'arborescence organisée par catégorie des packages. Cette arborescence est stockée par défaut dans le dossier **/usr/portage/** dont voici un exemple :

/usr/portage/www-apache
/usr/portage/www-apps
/usr/portage/www-client
/usr/portage/www-misc

Dans chaque catégorie, on retrouve un dossier par package disponible :

/usr/portage/www-client/chromium
/usr/portage/www-client/firefox
/usr/portage/www-client/opera

On voit que firefox et opera font partie de la catégorie _www-client_, leur nom complet de package sous Gentoo est :

- www-client/firefox
- www-client/opera

Bien sûr, on pourra aussi les appeler par leur petit nom mais il est important de noter qu'il est possible que deux packages aient le même nom s'ils font partie d'une arborescence différente. Mieux vaut donc toujours les appeler par leur nom complet.

# Les commandes

Toutes les commandes suivantes font partie de portage et permettent de le manipuler. La plus connue est sans aucun doute **emerge.**

/usr/bin/ebuild
/usr/bin/egencache
/usr/bin/emerge
/usr/bin/portageq
/usr/bin/quickpkg
/usr/bin/repoman

/usr/sbin/archive-conf
/usr/sbin/dispatch-conf
/usr/sbin/emaint
/usr/sbin/emerge-webrsync
/usr/sbin/env-update
/usr/sbin/etc-update
/usr/sbin/fixpackages
/usr/sbin/regenworld
/usr/sbin/update-env
/usr/sbin/update-etc

Dans un prochain post, je parlerai de l'utilisation des principales commandes de portage et de leur configuration.
