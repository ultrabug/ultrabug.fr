# EuroPython 2015

## Designing a scalable and distributed application

- [Download the slides](https://ep2017.europython.eu/media/conference/slides/using-service-discovery-a-distributed-application.pdf)
- [Watch the video](https://www.youtube.com/watch?v=WN_890QPhNA)

![](../images/2017-12-22-143412_1189x887_scrot-300x224.png)

One of the key aspect to keep in mind when developing a scalable
application is its faculty to grow easily. But while we're used to
take advantage of scalable backend technologies such as mongodb or
couchbase, scaling automatically our own application core is
usually another story.

In this talk I will **explain and showcase** a distributed web
application design based on consul and uWSGI and its consul
plugin. This design will cover the key components of a **distributed and**
**scalable application**:

- **Automatic service registration and discovery** will allow your application to grow itself automatically.
- Health checking and service unregistration will allow your application to be fault tolerant, highly available and to shrink itself automatically.
- A **distributed Key/Value storage** will allow you to (re)configure your distributed application nodes at once.
- **Multi-Datacenter** awareness will allow your application to scale around the world easily.
