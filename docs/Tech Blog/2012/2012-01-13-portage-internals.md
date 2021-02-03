---
title: "Portage internals"
date: "2012-01-13"
categories: 
  - "linux"
tags: 
  - "ebuild"
  - "gentoo"
  - "portage"
---

Maintenant que nous savons ce qu'est [Portage](http://www.ultrabug.fr/portage-basics/ "Portage basics"), comprenons simplement comment il fonctionne. Que se passe-t'il lorsque l'on veut installer un package, et d'ailleurs ça ressemble à quoi un **package** sous Gentoo ?

# Les ebuilds

Les packages disponibles dans l'arbre portage sont représentés par des fichiers appelés **ebuilds**. Les **ebuilds** contiennent toutes les informations nécessaires à la manipulation du package en question par portage (où télécharger les sources, quelle licence protège le logiciel, quelle est l'URL du projet, etc...).

Pour toute action vis à vis d'un **package**, portage se base sur les informations des **ebuilds** correspondants. Je dis de**s** ebuild**s** car un ebuild contient aussi la version du package qu'il représente. Il y a donc autant de fichiers ebuild que de versions disponibles d'un  package. Prenons l'exemple du package www-client/firefox :

$ ls /usr/portage/www-client/firefox

firefox-3.6.20.ebuild
firefox-3.6.22.ebuild
firefox-8.0.ebuild
firefox-9.0.ebuild

Les versions 3.6.20, 3.6.22, 8.0 et 9.0 sont donc disponibles sur portage. Si nous voulions des informations supplémentaires ou installer une de ces versions de firefox, portage n'aurait qu'à exécuter les instructions contenues dans le fichier ebuild correspondant, et voilà !

Quand Mozilla sortira firefox 10, un développeur ou contributeur Gentoo devra créer l'ebuild pour cette version afin qu'il soit disponible dans portage, il est donc crucial de tenir sa liste d'ebuilds à jour sur son système.

# Synchroniser portage

Mettre à jour portage, c'est donc mettre à jour la liste des ebuilds disponibles sur son système !

\# emerge --sync

Le fameux sync **télécharge les nouveaux** ebuilds et **supprime les obsolètes** pour nous, c'est grâce à cela que nous disposerons du nouveau firefox quand il sortira, et il en va bien sûr de même pour tous les packages.

Les développeurs et contributeurs Gentoo tiennent ensemble à jour un arbre portage commun qui est téléchargé et répliqué par des serveurs qu'on appelle **mirrors** (le terme mirroir signifie qu'ils contiennent une copie exacte de l'arbre de développement). Tous les utilisateurs répliquent à leur tour leur arbre portage local (par défaut dans **/usr/portage/**) en se connectant sur un de ces serveurs mirrors lors du sync.

A l'heure où j'écris ces lignes, le _portage tree_ contient **15459 packages** représentant **29931 ebuilds !**
