---
title: "My views on Python"
date: "2012-11-02"
categories: 
  - "linux"
tags: 
  - "development"
  - "python"
---

We're having a pretty hot debate in my company about the core development language we would like to embrace in order to enhance our work flow and unlock both our innovation and development iteration.

I thought of doing a blog post instead of writing an email summarizing my point of view about why we should choose python in case it could help other people to make their own mind or at least understand mine. I don't want to be dragged into the typical "language x VS language y" type of post as there are a lot of those already but instead focus on specific use cases. Anyway, to be totally transparent with you, dear reader, I have to tell you that the main "_opponent_" we're considering is Javascript / node.js.

## Python is easy to learn and write

I work for an online marketing/advertising company and we have four different IT/development teams with specific work to do.  That means that we all have our own constraints to take into account and we use different technologies / languages to achieve them. Opening a debate on a development language rationalization thus means that people will have to be able to learn the one we will choose, the quicker the better.

Well let's be honest, python is not widely taught on IT schools so our guys definitely WILL have to learn it. But python is one of the most **simple** language to learn as you can quickly test and make progress. This mainly comes from its coding syntax which makes the code cleaner and easy to read, also the language's keywords are simple to remember, no boring brackets or semicolons to drive you crazy. Python is about coding **clean** and instinctively.

A simple and straightforward syntax is very important to me because :

- it is easier to read
- it is easier to maintain
- your code is lighter
- you spend less time coding so you spend more time thinking

## Python everywhere

When choosing your core language, you must make sure you can **rely** on it today and tomorrow **for a wide range of use cases**. I find it very interesting to have a look at a list of its [application domains](http://www.python.org/about/apps/) as it does really show that with this language at our core, we would be able to achieve anything.

The **versatility** of python is my main argument in favor of its adoption. This is a **mature** and **proven** language with a lot of **libraries** and **frameworks** to suit all our present and future needs. It is widely **supported** on an extensive set of platforms and I can't think of an open-source project not supporting python right from the start.

At this point, I will quote the folks at [AppNexus from their conference in the recent PyData NYC 2012](http://nyc2012.pydata.org/abstracts/#appnexus) :

_"Python's versatility allows us to use it both for offline analytical tasks as well as production system development. Doing so allows us to bridge the gap between prototypes and production by relying on the same code libraries and frameworks for both, thereby tightening our innovation loop"._ 

They say python helped them grow very rapidly and efficiently by permitting them to focus on innovation, needless to say that I share their point of view and would love to see this happening in my company.

## Python use cases in my company

Now let's talk about our present and projected use cases. This is not an exhaustive list as I want to keep it simple and demonstrate the versatility I just talked about.

### Scripting and automation

I am a sysadmin and I am lazy. Nothing new here okay, but that's how I met python a bunch of years ago. At that time my company's infrastructure became more complex everyday as was growing very rapidly. New servers were arriving and provided new functionalities and new technologies which lead more and more to heterogeneity in the things we had to monitor, automate and configure.

Python is a sysadmin's heaven with all its libraries capable of handling complex tasks easily, even in our cluster environments where you have to deal with parallel and high availability computing. This is a big relief to know that whatever the task you're asked to carry you can safely say : "python can do it". The keyword here is **efficiency**.

### Complete and complex applications

A lot of **modern** and cross-platform applications are written in python or based on it. I for one wrote an email parsing software a few years ago and it's still kicking in production, its maintenance is easy and it has evolved smoothly with our growth and needs.

Another thing I like about this language is that it's **fast** and can benefit from a semi-compiled "byte-code" which speeds up your application. No, python is not C++ and speed is not it's biggest advantage of course but it's really fast enough to compete with others easily.

Let's sample some famous [software written in python](http://en.wikipedia.org/wiki/List_of_Python_software) :

- **BitTorrent**, original client, along with several derivatives
- **Dropbox**, a web-based file hosting service
- **OpenStack**, a cloud computing IaaS platform
- **Portage**, the heart of Gentoo Linux
- **Ubuntu** Software Center, a graphical package manager

### Web applications

Python also have some **solid** and very powerful librairies able to manage asynchronous, real-time and scalable web applications and services. We already do have some of those robust web apps running in production and python demonstrates everyday all of the strenghts I already talked about here. We use librairies such as **gevent** along with web frameworks like **flask** and message queuing with **zeromq**. Someday I may write a post about our python web stack, it may be interesting to share about it.

I have been able to recode a web app written in .NET very quickly while enhancing it in every way possible. It is way faster, reliable, **fault tolerant** and maintainable that it was before. Thanks to python we have a **short development iteration** which proves itself everyday as the application grows and is capable to meet and achieve any new challenge we're asked to take care of. I'm convinced that no other language could have been so powerful and versatile than python to do so.

We're not the only ones thinking and experiencing this of course, [still in the list](http://en.wikipedia.org/wiki/List_of_Python_software) we can see :

- **Google** uses Python for many tasks including the backends of web apps such as Google Groups, Gmail, and Google Maps, as well as for some of its search-engine internals
- **AppNexus** uses Python for some of their web apps backend
- **YouTube** uses Python "to produce maintainable features in record times, with a minimum of developers"
- **Yahoo!** Groups uses Python "to maintain its discussion groups"

That's some big players indeed and it's interesting to see they use python for their web app **backends**.

## Conclusion

I am not a software developer as I never took strong development courses at school. I am a sysadmin of complex, clustered and heterogeneous environments so this affects my development standards and point of view in a way that my expectations will surely be different from a pure developer.

My main concerns can be defined with words like **proven, easy, clean, versatile, maintainable, fast (to code and execute), scalable, fault-tolerant and cross-platform**. All of my choices have been based on those standards and concerns and I think they apply well in our debate because I chose Python to meet them all and I've never been disappointed or limited by it.

I hope this post reflects my thoughts and helped you understand them. I will tell you about the result and the decision my company made on this debate.
