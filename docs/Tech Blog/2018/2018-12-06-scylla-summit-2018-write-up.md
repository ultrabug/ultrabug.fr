---
title: "Scylla Summit 2018 write-up"
date: "2018-12-06"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "scylla"
---

It's been almost one month since I had the chance to attend and speak at **[Scylla Summit 2018](https://www.scylladb.com/scylla-summit-2018/)** so I'm relieved to finally publish a short write-up on the key things I wanted to share about this wonderful event!

![](images/DrQOptgXgAAcWIX.jpg)

## Make Scylla boring  

This statement of Glauber Costa sums up what looked to me to be the main driver of the engineering efforts put into Scylla lately: making it work so consistently well on any kind of workload that it's boring to operate :)  
  
I will follow up on this statement to highlight the things I heard and (hopefully) understood during the summit. I hope you'll find it insightful.  

### Reduced operational efforts  

The thread-per-core and queues design still has a lot of possibilities to be leveraged.  
  
The recent addition of **RPC streaming** capabilities to seastar allows a [drastic reduction](https://www.scylladb.com/2018/08/14/upcoming-improvements-scylla-streaming/) in the time it takes the cluster to grow or shrink (data rebalancing / resynchronization).  
  
**Incremental compaction** is also very promising as this background process is one of the most expensive there is in the database's design.  
  
I was happy to hear that **scylla-manager** will soon be made available and free to use with basic features while retaining more advanced ones for enterprise version (like backup/restore).  
I also noticed that the current version was not supporting SSL enabled clusters to store its configuration. So I directly asked Michał for it and I'm glad that it will be released on version 1.3.1. 

### Performant multi-tenancy  

Why choose between [real-time OLTP & analytics OLAP](https://sched.co/GcEr) workloads?  
  
The goal here is to be able to run both on the same cluster by giving users the ability to assign "SLA" **shares** to ROLES. That's basically like pools on Hadoop at a much finer grain since it will create dedicated queues that will be weighted by their share.  
  
Having **one queue per usage** and full accounting will allow to limit resources efficiently and users to have their say on their latency SLAs.  
  
But Scylla also has a lot to do in the background to run smoothly. So while this design pattern was already applied to tamper compactions, a lot of work has also been done on automatic flow control and back pressure.  
  
For instance, Materialized Views are updated asynchronously which means that while we can interact and put a lot of pressure on the table its based on (called the Main Table), we could overwhelm the background work that's needed to keep MVs View Tables in sync. To mitigate this, a smart **[back pressure](https://www.scylladb.com/2018/12/04/worry-free-ingestion-flow-control/)** approach was developed and will throttle the clients to make sure that Scylla can manage to do everything at the best performance the hardware allows!  
  
I was happy to hear that work on **tiered storage** is also planned to better optimize disk space costs for certain workloads.  
  
Last but not least, **columnar storage** optimized for time series and analytics workloads are also something the developers are looking at.  

### Latency is expensive  

If you care for latency, you might be happy to hear that a new polling API (named [IOCB_CMD_POLL](https://old.lwn.net/Articles/742978/)) has been contributed by Christoph Hellwig and Avi Kivity to the 4.19 Linux kernel which avoids context switching I/O by using a shared ring between kernel and userspace. Scylla will be using it by default if the kernel supports it.  
  
The iotune utility has been upgraded since 2.3 to generate an [enhanced I/O](https://www.scylladb.com/2018/04/19/scylla-i-o-scheduler-3/) configuration.  
  
Also, persistent (disk backed) **[in-memory tables](https://sched.co/GcdR)** are getting ready and are very promising for latency sensitive workloads!  

### A word on drivers  

ScyllaDB has been relying on the Datastax drivers since the start. While it's a good thing for the whole community, it's important to note that the shard-per-CPU approach on data that Scylla is using is not known and leveraged by the current drivers.  
  
[Discussions](https://lists.apache.org/thread.html/7539f11b6e2e4c7841f0409f15a05b6d6e32cdf7ce6f92024d62f965@%3Cdev.cassandra.apache.org%3E) took place and it seems that Datastax will not allow the protocol to evolve so that drivers could discover if the connected cluster is shard aware or not and then use this information to be more clever in which write/read path to use.  
  
So for now ScyllaDB has been forking and developing their **shard aware** drivers for Java and Go (no Python yet... I was disappointed).  

### Kubernetes & containers  

The ScyllaDB guys of course couldn't avoid the Kubernetes frenzy so Moreno Garcia gave a lot of [feedback and tips](https://www.scylladb.com/2018/08/09/cost-containerization-scylla/) on how to operate Scylla on docker with minimal performance degradation.  
  
Kubernetes has been designed for stateless applications, not stateful ones and Docker does some automatic magic that have rather big performance hits on Scylla. You will basically have to play with affinities to dedicate one Scylla instance to run on one server with a "retain" reclaim policy.  
  
Remember that the official Scylla docker image runs with dev-mode enabled by default which turns off all performance checks on start. So start by disabling that and look at all the tips and literature that Moreno has put online!  

![](images/DrVXLqWXQAAJnmS-1024x329.jpg)

## Scylla 3.0  

A lot has been [written on it already](https://www.scylladb.com/2018/11/08/overheard-at-scylla-summit-2018/) so I will just be short on things that important to understand in my point of view.

- Materialized Views do back fill the whole data set  
    - this job is done by the view building process
    - you can watch its progress in the **system_distributed.view_build_status** table  
        
- Secondary Indexes are Materialized Views under the hood  
    - it's like a reverse pointer to the primary key of the Main Table  
        
    - so if you read the whole row by selecting on the indexed column, two reads will be issued under the hood: one on the indexed MV view table to get the primary key and one on the main table to get the rest of the columns  
        
    - **so if your workload is mostly interested by the whole row, you're better off creating a complete MV to read from than using a SI**
    - this is even more true if you plan to do range scans as this double query could lead you to read from multiple nodes instead of one  
        
- [Range scan](https://www.scylladb.com/2018/11/01/more-efficient-range-scan-paging-with-scylla-3-0/) is way more performant
    - ALLOW FILTERING finally allows a great flexibility by providing **server-side filtering**!

![](images/DrcOcTSUUAAJSVi-1024x248.jpg)

## Random notes

Support for **LWT** (lightweight transactions) will be relying on a future implementation of the Raft consensus algorithm inside Scylla. This work will also benefits Materialized Views consistency. Duarte Nunes will be the one working on this and I envy him very much!  

Support for **search** workloads is high in the ScyllaDB devs priorities so we should definitely hear about it in the coming months.

Support for "**mc**" sstables (new generation format) is done and will reduce storage requirements thanks to metadata / data compression. Migration will be transparent because Scylla can read previous formats as well so it will upgrade your sstables as it compacts them.  

ScyllaDB developers have not settled on how to best implement **CDC**. I hope they do rather soon because it is crucial in their ability to integrate well with Kafka!  

Materialized Views, Secondary Indexes and filtering will benefit from the work on **partition key and indexes intersections** to avoid server side filtering on the coordinator. That's an important optimization to come!

Last but not least, I've had the pleasure to discuss with Takuya Asada who is the packager of Scylla for RedHat/CentOS & Debian/Ubuntu. We discussed **Gentoo Linux packaging** requirements as well as the recent and promising work on a relocatable package. We will collaborate more closely in the future!
