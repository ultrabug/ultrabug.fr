---
title: "State of the event log architecture enhancements"
date: "2012-05-25"
categories: 
  - "linux"
tags: 
  - "cee"
  - "json"
  - "lumberjack"
  - "rsyslog"
  - "syslog"
  - "syslog-ng"
---

Interesting stuff is happening on the event log (syslog) community and more precisely on the topic of **syslog format extension and structuring syslog data**.

As of today there's no real standard on how to format and structure data on a syslog message. Every project has its own log message structure and syntax (qmail and postfix don't log a mail delivery failure the same way for example), so we rely on parsers to extract any given data from a log message because the syslog software has no way to do it for us. I for one have coded a postfix log parser and believe me it's not a pleasant thing to do and maintain !

The main idea about structuring syslog messages is to represent them using **JSON** along with the current free form strings to prevent backward compatibility breakage. To achieve this, we need to normalize and extend this format so that syslog software such as **rsyslog** and **syslog-ng** can directly understand them. That's where **CEE-enhanced messages** and **Lumberjack** kick in.

# CEE-enhanced messages

[The CEE project](http://cee.mitre.org/) aims at defining a syntax which **extends** the current log message format while being compatible with all the currently and widely used log frameworks or the well known glibc's syslog() call. To achieve this the main idea is to use what is called a **cookie** before the **JSON representation of the data** we want to pass to the syslog software.

To make it simple, let's pretend we see this postfix log meaning that a queued mail has been removed from the queue (I removed the date etc to only focus on the message part) :

CAA3B607DA: removed

The equivalent CEE-enhanced message _could_ (this would be up to postfix) be represented as :

@cee: {"id":"CAA3B607DA", "removed":"true"}

- @cee: is what is called the cookie which tells the syslog software that this message is using the CEE-enhanced syntax

I guess you already see how handy this would be and how we could then rely on the syslog software to automagically use our favorite storage backend to store this structured data (think mongoDB).

More information on the handy and quick [video presentation by Rainer Gerhards](http://blog.gerhards.net/2012/03/what-is-cee-enhanced-syslog.html) and [his article about it](http://blog.gerhards.net/2012/03/cee-enhanced-syslog-defined.html).

# The Lumberjack project

So now how do we format the JSON part ? Could we have other types such as booleans and integers directly interpreted by the syslog software ? Well this needs definitions and standardization proposals, that's what [project Lumberjack](https://fedorahosted.org/lumberjack/) is for.

Have a nice read on [Lumberjack origins on Rainer Gerhards's blog](http://blog.gerhards.net/2012/02/announcing-project-lumberjack.html).
