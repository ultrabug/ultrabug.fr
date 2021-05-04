---
title: "mongoDB : export based on objectIDs' timestamp"
date: "2012-06-12"
categories: 
  - "linux"
tags: 
  - "mongodb"
  - "mongoexport"
  - "nosql"
---

I needed to export a set of data from a **mongoDB** collection based on their **objectIDs' (_id) timestamp** using **mongoexport**. The [mongoexport documentation](http://www.mongodb.org/display/DOCS/mongoexport) is everything but helpful on the subject so I had to find a workaround to answer this simple question : **_"export  all documents inserted yesterday on this collection in a CSV format"_**.

# Relevant mongoexport options

-  --host : specify the mongoDB host
- \--username / --pasword : if you're using authentication on your server
- \-d : database to use
- \-c : collection to use
- \--fields : fields you want to export (omit for all)
- **\--query** : the actual query selecting the result set you want to export
- \--csv : export in a CSV format

**The date range query workaround**

So the hard part is to actually ask **mongoexport** to only return the documents in the desired time frame using an **objectID** compliant **query**. I overcame this problem using a simple but efficient python script generating the query for me.

#!/usr/bin/python

# using pymongo-2.2
from bson.objectid import ObjectId
import datetime

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
start_date = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
end_date = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
oid_start = ObjectId.from_datetime(start_date)
oid_stop = ObjectId.from_datetime(end_date)

print '{ "_id" : { "$gte" : { "$oid": "%s" }, "$lt" : { "$oid": "%s" } } }' % ( str(oid_start), str(oid_stop) )

This script just prints out a command line compliant representation of the **objectIDs** for yesterday and today. So this query will select exactly what I wanted : _**all yesterday's objectIDs.**_ Example :

__{ "_id" : { "$gte" : { "$oid": "4fd535000000000000000000" } , "$lt" : { "$oid": "4fd686800000000000000000" } } }__

# Using mongoexport

We then can simply use **mongoexport** from the shell by issuing (I left the optional parameters out) :

$ mongoexport -h localhost -d myDatabase -c theCollection --query "$(python oid.py)" --csv

Et voilà !

I guess there must be a cleaner way to do it out there, but I was unable to find it in my limited search time frame, so comment this post if you have a better solution please !
