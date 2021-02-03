---
title: "Evaluating ScyllaDB for production 1/2"
date: "2018-01-23"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "nosql"
  - "scylla"
---

I have recently been conducting a quite deep evaluation of [ScyllaDB](http://www.scylladb.com/) to find out if we could benefit from this database in some of our intensive and latency critical data streams and jobs.

I'll try to share this great experience within two posts:

1. The first one (you're reading) will walk through how to prepare yourself for a successful Proof Of Concept based evaluation with the help of the ScyllaDB team.
2. The second post will cover the technical aspects and details of the POC I've conducted with the various approaches I've followed to find the most optimal solution.

But let's start with how I got into this in the first place...

* * *

# Selecting ScyllaDB

[I got interested in ScyllaDB because of its philosophy and engagement](https://www.ultrabug.fr/scylladb-meets-gentoo-linux/) and I quickly got into it by being a modest contributor and its Gentoo Linux packager (not in portage yet).

![](images/mascot.png)

Of course, I didn't pick an interest in that technology by chance:

We've been using MongoDB in (mass) production at work for a very very long time now. I can easily say we were early MongoDB adopters. But there's no wisdom in saying that MongoDB is not suited for every use case and the Hadoop stack has come very strong in our data centers since then, with a predominance of Hive for the heavy duty and data hungry workflows.

One thing I was never satisfied with MongoDB was its primary/secondary architecture which makes you lose write throughput and is even more horrible when you want to set up what they call a "cluster" which is in fact some mediocre abstraction they add on top of replica-sets. To say the least, it is inefficient and cumbersome to operate and maintain.

So I obviously had Cassandra on my radar for a long time, but I was pushed back by its Java stack, heap size and silly tuning... Also, coming from the versatile MongoDB world, Cassandra's CQL limitations looked dreadful at that time...

The day I found myself on ScyllaDB's webpage and read their promises, I was sure to be challenging our current use cases with this interesting sea monster.

* * *

# Setting up a POC with the people at ScyllaDB

Through my contributions around my packaging of ScyllaDB for Gentoo Linux, I got to know a bit about the people behind the technology. They got interested in why I was packaging this in the first place and when I explained my not-so-secret goal of challenging our production data workflows using Scylla, they told me that they would love to help!

I was a bit surprised at first because this was the first time I ever saw a real engagement of the people behind a technology into someone else's POC.

Their pitch is simple, they will help (for free) anyone conducting a serious POC to make sure that the outcome and the comprehension behind it is the best possible. It is a very mature reasoning to me because it is easy to make false assumptions and conclude badly when testing a technology you don't know, even more when your use cases are complex and your expectations are very high like us.

Still, to my current knowledge, they're the only ones in the data industry to have this kind of logic in place since the start. So I wanted to take this chance to thank them again for this!

The POC includes:

- **no bullshit**, simple tech-to-tech relationship
- **a private slack channel** with multiple ScyllaDB's engineers
- **video calls** to introduce ourselves and discuss our progress later on
- **help in schema design** and logic
- **fast answers** to every question you have
- **detailed explanations** on the internals of the technology
- hardware **sizing help and validation**
- funny comments and French jokes (ok, not suitable for everyone)

![](images/2018-01-22-181625_402x309_scrot.png)

 

 

 

 

 

 

 

 

 

* * *

# Lessons for a successful POC

As I said before, you've got to be serious in your approach to make sure your POC will be efficient and will lead to an unbiased and fair conclusion.

This is a list of the main things I consider important to have prepared before you start.

## Have some background

Make sure to read some literature to have the key concepts and words in mind before you go. It is even more important if like me you do not come from the Cassandra world.

I found that the [Cassandra: The Definitive Guide](http://shop.oreilly.com/product/0636920010852.do) book at O'Reilly is a great read. Also, make sure to go around [ScyllaDB's documentation](http://docs.scylladb.com/).

![](images/lrg-150x150.jpg)

## Work with a shared reference document

Make sure you share with the ScyllaDB guys **a clear and detailed document explaining exactly what you're trying to achieve and how you are doing it today** (if you plan on migrating like we did).

I made a google document for this because it felt the easiest. This document will be updated as you go and will serve as a **reference** for everyone participating in the POC.

This shared reference document is very important, so if you don't know how to construct it or what to put in it, here is how I structured it:

1. **Who's participating at <your company>**
    - photo + name + speciality
2. **Who's participating at ScyllaDB**
3. **POC hardware**
    - if you have your own bare metal machines you want to run your POC on, give every detail about their number and specs
    - if not, explain how you plan to setup and run your scylla cluster
4. **Reference infrastructure**
    - give every details on the technologies and on the hardware of the servers that are currently responsible for running your workflows
    - explain your clusters and their speciality
5. **Use case #1 : <name>**
    - **Context**
        - give context about your use case by explaining it without tech words, think from the business / user point of view
    - **Current implementations**
        - that's where you get technical
        - technology names and where they come into play in your current stack
        - insightful data volumes and cardinality
        - current schema models
    - **Workload related to this use case**
        - queries per second per data source / type
        - peek hours or no peek hours?
        - criticality
    - **Questions we want to answer to**
        - remember, the NoSQL world is lead by query-based-modeling schema design logic, cassandra/scylla is no exception
        - write down the real questions you want your data model(s) to be able to answer to
        - group them and rate them by importance
    - **Validated models**
        - this one comes during the POC when you have settled on the data models
        - write them down, explain them or relate them to the questions they answer to
        - copy/paste some code showcasing how to work with them
    - **Code examples**
        - depending on the complexity of your use case, you may have multiple constraints or ways to compare your current implementation with your POC
        - try to explain what you test and copy/paste the best code you came up with to validate each point

## Have monitoring in place

ScyllaDB provides a [monitoring platform based on Docker, Prometheus and Grafana](https://github.com/scylladb/scylla-grafana-monitoring) that is efficient and simple to set up. I strongly recommend that you set it up, as it provides valuable insights almost immediately, and on an ongoing basis.

Also you should strive to give access to your monitoring to the ScyllaDB guys, if that's possible for you. They will provide with a fixed IP which you can authorize to access your grafana dashboards so they can have a look at the performances of your POC cluster as you go. You'll learn a great deal about ScyllaDB's internals by sharing with them.

## Know when to stop

The main trap in a POC is to work without boundaries. Since you're looking for the best of what you can get out of a technology, you'll get tempted to refine indefinitely.

So this is good to have at least an idea on the minimal figures you'd like to reach to get satisfied with your tests. You can always push a bit further but not for too long!

## Plan some high availability tests

Even if you first came to ScyllaDB for its speed, make sure to test its high availability capabilities based on your experience.

Most importantly, make sure you test it within your code base and guidelines. How will your code react and handle a failure, partial and total? I was very surprised and saddened to discover so little literature on the subject in the Cassandra community.

## POC != production

Remember that even when everything is right on paper, production load will have its share of surprises and unexpected behaviours. So keep a good deal of flexibility in your design and your capacity planning to absorb them.

## Make time

Our POC lasted almost 5 months instead of estimated 3, mostly because of my agenda's unwillingness to cooperate...

As you can imagine this interruption was not always optimal, for either me or the ScyllaDB guys, but they were kind not to complain about it. So depending on how thorough you plan to be, make sure you make time matching your degree of demands. The reference document is also helpful to get back to speed.

* * *

# Feedback for the ScyllaDB guys

Here are the main points I noted during the POC that the guys from ScyllaDB could improve on.

They are subjective of course but it's important to give feedback so here it goes. I'm fully aware that everyone is trying to improve, so I'm not pointing any fingers at all.

I shared those comments already with them and they acknowledged them very well.

## More video meetings on start

When starting the POC, try to have some **pre-scheduled video meetings** to set it right in motion. This will provide a good pace as well as making sure that everyone is on the same page.

## Make a POC kick starter questionnaire

Having a minimal plan to follow with some key points to set up just like the ones I explained before would help. Maybe also a minimal questionnaire to make sure that the key aspects and figures have been given some thought since the start. This will raise awareness on the real answers the POC aims to answer.

To put it simpler: **some minimal formalism helps to check out the key aspects and questions.**

## Develop a higher client driver expertise

This one was the most painful to me, and is likely to be painful for anyone who, like me, is not coming from the Cassandra world.

Finding good and strong code examples and guidelines on the client side was hard and that's where I felt the most alone. This was not pleasant because a technology is definitely validated through its usage which means on the client side.

Most of my tests were using **python** and the **python-cassandra** driver so I had tons of questions about it with no sticking answers. Same thing went with the **spark-cassandra-connector** when using **scala** where some key configuration options (not documented) can change the shape of your results drastically (more details on the next post).

## High Availability guidelines and examples

This one still strikes me as the most awkward on the Cassandra community. I literally struggled with finding clear and detailed explanations about how to handle failure more or less gracefully with the python driver (or any other driver).

This is kind of a disappointment to me for a technology that position itself as **highly available**... I'll get into more details about it on the next post.

## A clearer sizing documentation

Even if there will never be a magic formula, there are some rules of thumb that exist for sizing your hardware for ScyllaDB. They should be written down more clearly in a maybe dedicated documentation ([sizing guide is labeled as admin guide at time of writing](http://docs.scylladb.com/admin/)).

Some examples:

- RAM per core ? what is a core ? relation to shard ?
- Disk / RAM maximal ratio ?
- Multiple SSDs vs one NMVe ?
- Hardware RAID vs software RAID ? need a RAID controller at all ?

Maybe even provide a bare metal complete example from two different vendors such as DELL and HP.

# What's next?

In the next post, I'll get into more details on the POC itself and the technical learnings we found along the way. This will lead to the final conclusion and the next move we engaged ourselves with.
