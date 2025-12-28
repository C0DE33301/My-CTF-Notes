---
layout: default
title: Investigating Windows
parent: Easy
nav_order: 2
---

# Investigating Windows

## Task 1 | Investigating Windows
### Connect to the machine using `Remote Desktop Protocol (RDP)`
- Open, Microsoft's `Remote Desktop Connection` applications.
- Username: `Administrator`
- Password: `letmein123!`

### Question 1
```diff
+ Whats the version and year of the windows machine?

+ Right click the win key > System > Windows Edition
+ Windows Server 2016
```
### Question 2
```diff
+ Which user logged in last?

+ Event Viewer > Windows Logs > Security > Actions > Filter Current Log > 4624
+ Administrator
```
### Question 3
```diff
+ When did John log onto the system last?

+ 03/02/2019 5:48:32 PM
```
**Open**, `CMD`
- **Type**: `net user John`
    - **Find**: `Last logon`
### Question 4
```diff
+ What IP does the system connect to when it first starts?

+ 10.34.2.3
```
```
PsExec v1.98 - Execute processes remotely
Copyright (C) 2001-2010 Mark Russinovich             
Sysinternals - www.sysinternals.com              
Connecting to 10.34.2.3.
```
### Question 5
```diff
+ What two accounts had administrative privileges (other than the Administrator user)?

+ Guest, Jenny
```
**Open**, `CMD`
- **Type**: `net user Jenny`
    - **Find**: `Local Group Memberships`
- **Type**: `net user guest`
    - **Find**: `Local Group Memberships`
### Question 6
```diff
+ Whats the name of the scheduled task that is malicous.

+ clean file system
```
**Select**, `Task Scheduler` > `Task Scheduler Library`
- **Name**: `clean file system`
### Question 7
```diff
+ What file was the task trying to run daily?

+ nc.ps1
```
**Select**, `Task Scheduler` > `Task Scheduler Library`
- **Name**: `clean file system`
- **Navigate**: `Actions` > `Start a program`
**File Location**
```ps1
Get-ChildItem -Path C:\ -Filter nc.ps1 -Recurse
```
```
Directory: C:\TMP
Mode                LastWriteTime         Length Name  
----                -------------         ------ ----  
-a----              3/2/2019 4:37 PM    37640  nc.ps1
```
### Question 8
```diff
+ What port did this file listen locally for?

+ 1348
```
**Select**, `Task Scheduler` > `Task Scheduler Library`
- **Name**: `clean file system`
- **Navigate**: `Actions` > `Start a program`
### Question 9
```diff
+ When did Jenny last logon?

+ Never
```
**Open**, `CMD`
- **Type**: `net user Jenny`
    - **Find**: `Last logon`
### Question 10
```diff
+ At what date did the compromise take place?

+ 03/02/2019
```
View the date of `C:\TMP` dir
### Question 11
```diff
+ During the compromise, at what time did Windows first assign special privileges to a new logon?

+ 03/02/2019 4:04:49 PM
```
**View**
- `Event Viewer` > `Windows Logs` > `Application` > `Event ID`:`1016` & `Source`:`Security-SPP`
### Question 12
```diff
+ What tool was used to get Windows passwords?

+ mimikatz
```
**Run**, `cat .\mim-out.txt`
```
  .#####.   mimikatz 2.0 alpha (x86) release "Kiwi en C" (Feb 16 2015 22:17:52)  
 .## ^ ##.
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                     with 15 modules * * */   

mimikatz(powershell) # sekurlsa::logonpasswords                                 
```
### Question 13
```diff
+ What was the attackers external control and command servers IP?

+ 76.32.97.132
```
```ps1
cat C:\Windows\System32\drivers\etc\hosts
```
### Question 14
```diff
+ What was the extension name of the shell uploaded via the servers website?

+ .jsp
```
```
C:\inetpub\wwwroot\b.jsp
```
### Question 15
```diff
+ What was the last port the attacker opened?

+ 1337
+ Windows Firewall with Advanced Security > Monitoring > Firewall > Name > Allow outside connections for development
```
### Question 16
```diff
+ Check for DNS poisoning, what site was targeted?

+ 76.32.97.132 www.google.com 
```
```ps1
cat C:\Windows\System32\drivers\etc\hosts
```