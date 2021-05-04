---
title: "Using uWSGI and Consul to design a distributed application"
date: "2014-08-14"
categories: 
  - "linux"
tags: 
  - "consul"
  - "gentoo"
  - "python"
  - "uwsgi"
---

## Foreword

Let's say we have to design an application that should **span across multiple datacenters** while being able to **scale** as easily as firing up a new vm/container without the need to update any kind of configuration.

Facing this kind of challenge is exciting and requires us to address a few key scaffolding points before actually starting to code something :

- having a robust and yet versatile application container to run our application
- having a datacenter aware, fault detecting and service discovery service

Seeing the title of this article, the two components I'll demonstrate are obviously uWSGI and Consul which can now [work together](https://github.com/ultrabug/uwsgi-consul-rfc) thanks to the [uwsgi-consul plugin](https://github.com/unbit/uwsgi-consul).

While this article example is written in python, you can benefit from the same features in all the [languages supported by uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/LanguagesAndPlatforms.html) which includes go, ruby, perl ad php !

## Our first service discovering application

The application will demonstrate how simple it is for a **client** to discover all the available **servers** running a specific **service** on a given **port**. The best part is that the services will be registered and deregistered automatically by uWSGI as they're loaded and unloaded.

The demo application logic is as follows :

1. uWSGI will load two **server** applications which are each responsible for providing the specified **service** on the given **port**
2. uWSGI will automatically **register** the configured **service** into Consul
3. uWSGI will also automatically **register** a health **check** for the configured **service** into Consul so that Consul will also be able to detect any failure of the **service**
4. Consul will then **respond** to any **client** requesting the **list** of the available **servers** (nodes) providing the specified **service**
5. The **client** will query Consul for the **service** and get either an empty response (no server available / loaded) or the list of the available servers

Et voilà, the client can dynamically detect new/obsolete servers and start working !

## Setting up uWSGI and its Consul plugin

On Gentoo Linux, you'll just have to run the following commands to get started (other users refer to the [uWSGI documentation](http://uwsgi-docs.readthedocs.org/en/latest/Install.html) or your distro's package manager). The plugin will be built by hand as I'm still not sure how I'll package the uWSGI external plugins...

$ sudo ACCEPT_KEYWORDS="~amd64" emerge uwsgi
$ cd /usr/lib/uwsgi/
$ sudo uwsgi --build-plugin https://github.com/unbit/uwsgi-consul
$ cd -

 

You'll have installed the [uwsgi-consul](https://github.com/unbit/uwsgi-consul) plugin which you should see here :

$ ls /usr/lib/uwsgi/consul_plugin.so
/usr/lib/uwsgi/consul_plugin.so

 

That's all we need to have uWSGI working with Consul.

## Setting up a Consul server

Gentoo users will need to add the _ultrabug_ overlay (use layman) and then install consul (other users refer to the [Consul documentation](http://www.consul.io/downloads.html) or your distro's package manager).

$ sudo layman -a ultrabug
$ sudo ACCEPT_KEYWORDS="~amd64" USE="web" emerge consul

 

Running the server and its UI is also quite straightforward. For this example, we will run it directly from a dedicated terminal so you can also enjoy the logs and see what's going on (Gentoo users have an init script and conf.d ready for them shall they wish to go further).

Open a new terminal and run :

$ consul agent -data-dir=/tmp/consul-agent -server -bootstrap -ui-dir=/var/lib/consul/ui -client=0.0.0.0

 

You'll see consul running and waiting for work. You can already enjoy the web UI by pointing your browser to [http://127.0.0.1:8500/ui/](http://127.0.0.1:8500/ui/).

## Running the application

To get this example running, we'll use the [uwsgi-consul-demo](https://github.com/ultrabug/uwsgi-consul-demo) code that I prepared.

First of all we'll need the [consulate](https://github.com/gmr/consulate) python library (available on pypi via pip). Gentoo users can just install it (also from the ultrabug overlay added before) :

$ sudo ACCEPT_KEYWORDS="~amd64" emerge consulate

 

Now let's clone the demo repository and get into the project's directory.

$ git clone git@github.com:ultrabug/uwsgi-consul-demo.git
$ cd uwsgi-consul-demo

 

First, we'll run the **client** which should report that no server is available yet. We will keep this terminal open to see the client detecting in real time the appearance and disappearance of the servers as we start and stop uwsgi :

$ python client.py 
no consul-demo-server available
[...]
no consul-demo-server available

 

Open a new terminal and get inside the project's directory. Let's have uWSGI load the two **servers** and register them in Consul :

$ uwsgi --ini uwsgi-consul-demo.ini --ini uwsgi-consul-demo.ini:server1 --ini uwsgi-consul-demo.ini:server2
[...]
\* server #1 is up on port 2001

\* server #2 is up on port 2002

[consul] workers ready, let's register the service to the agent
[consul] service consul-demo-server registered succesfully
[consul] workers ready, let's register the service to the agent
[consul] service consul-demo-server registered succesfully

 

Now let's check back our **client** terminal, hooray it has discovered the two servers on the host named drakar (that's my local box) !

consul-demo-server found on node drakar (xx.xx.xx.xx) using port 2002
consul-demo-server found on node drakar (xx.xx.xx.xx) using port 2001

## Expanding our application

Ok it works great on our local machine but we want to see how to add more servers to the fun and scale dynamically.

Let's add another machine (named _cheetah_ here) to the fun and have servers running there also while our client is still running on our local machine.

On _cheetah_ :

- install uWSGI as described earlier
- install Consul as described earlier

Run a **Consul agent** (no need of a server) and tell him to work with your already running consul server on your box (_drakar_ in my case) :

$ /usr/bin/consul agent -data-dir=/tmp/consul-agent -join drakar -ui-dir=/var/lib/consul/ui -client=0.0.0.0

_The **\-join** <your host or IP> is the important part._

 

Now run uWSGI so it starts and registers two new servers on _cheetah_ :

$ uwsgi --ini uwsgi-consul-demo.ini --ini uwsgi-consul-demo.ini:server1 --ini uwsgi-consul-demo.ini:server2

 

And check the miracle on your **client** terminal still running on your local box, the new servers have appeared and will disappear if you stop uwsgi on the _cheetah_ node :

consul-demo-server found on node drakar (xx.xx.xx.xx) using port 2001
consul-demo-server found on node drakar (xx.xx.xx.xx) using port 2002
consul-demo-server found on node cheetah (yy.yy.yy.yy) using port 2001
consul-demo-server found on node cheetah (yy.yy.yy.yy) using port 2002

## Go mad

Check the source code, it's so simple and efficient you'll cry ;)

I hope this example has given you some insights and ideas for your current or future application designs !
