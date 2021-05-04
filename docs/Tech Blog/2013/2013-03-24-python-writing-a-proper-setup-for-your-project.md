---
title: "Python : writing a proper setup for your project"
date: "2013-03-24"
categories: 
  - "linux"
tags: 
  - "python"
  - "setup"
---

For an open-source project to be adopted, it must be easy to install and test it. Before publicly releasing py3status I thus had to figure out how to get my python project installed properly for every user who would be interested in it.

The common and most efficient way of writing a setup process in python is by using the **setuptools** package and writing your own **setup.py** file. Doing so is not hard at all as there are quite a bunch of examples you can start from but my challenge was that py3status is not a library you install and then import on your python code, instead it must be seen and used as an executable available for all users (something like /usr/bin/py3status). I'll cover the steps I used to achieve this kind of installation.

## setup.py basics

You can see the setup.py file just like any other python program you write where you import the functions you need from setuptools.

import os
from setuptools import find_packages, setup

Basically, a setup.py file is just a call to **setup** with a fair amount of parameters depending on the size and complexity of your project. Let's see a basic usage with no real magic.

setup(
	name='py3status',
	version='0.5',
	url='https://github.com/ultrabug/py3status/wiki',
	download_url='https://github.com/ultrabug/py3status',
	license='BSD',
	author='Ultrabug',
	author_email='ultrabug@sikritdomain.com',
	description='py3status is an extensible i3status wrapper written in python',
	long_description='this is a very long description which im writing for example',
	platforms='any',
	)

As you can see those parameters are just fields describing your project but there are of course more parameters you can use to become more specific about it such as which other packages it depends from or special operations to be made upon installation.

## classifiers

As with a literal description, you must categorize your project so that it will be correctly understood by automatic classifiers for example. The classifiers parameter is a list of those categories which [you can find a list here](https://pypi.python.org/pypi?%3Aaction=list_classifiers).

	classifiers=[
		'License :: OSI Approved :: BSD License',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Desktop Environment :: Window Managers :: i3wm',
		],

## getting an executable from your python program

As I explained earlier, py3status must be used as an executable available in the users' PATH just like any other binary or commands on the system. I was thrilled to discover that achieving this is a piece of cake using setuptools, you just have to use the **entry_points** parameter and [it will be taken care of for you](http://peak.telecommunity.com/DevCenter/setuptools#automatic-script-creation).

entry_points={
		'console_scripts': [
			'py3status = py3status:main',
			]
		},

So here I'm asking setuptools to create a script which will execute py3status' **main** function. It will generate a python program that just does that, call it py3status, place it in /usr/bin and make it executable. Et voilà ! An important thing to note is that it also works in Windows and that's how you'll get a **.exe** from your python code !

Learn more on this subject by reading the excellent [documentation on how to get started with setuptools](http://pythonhosted.org/an_example_pypi_project/setuptools.html).
