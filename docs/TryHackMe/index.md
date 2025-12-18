---
title: TryHackMe
layout: default
---

- [Advent Of Cyber 25](Advent%20Of%20Cyber%2025/index.md "Soon, Jan 2026")

    0. [Advent Of Cyber Prep Track](Advent%20Of%20Cyber%2025/0-Advent-Of-Cyber-Prep-Track.md)
    1. [Linux CLI - Shells Bells](Advent%20Of%20Cyber%2025/1-Linux-CLI-Shells-Bells.md)
    1. [Phishing - Merry Clickmas](Advent%20Of%20Cyber%2025/2-Phishing-Merry-Clickmas.md)
    1. [Splunk Basics - Did you SIEM?](Advent%20Of%20Cyber%2025/3-Splunk-Basics-Did-you-SIEM.md)
    1. [AI in Security - old sAInt nick](Advent%20Of%20Cyber%2025/4-AI-in-Security-old-sAInt-nick.md)
    1. [IDOR - Santa’s Little IDOR](Advent%20Of%20Cyber%2025/5-IDOR-Santa’s-Little-IDOR.md)
    1. [Malware Analysis - Egg-xecutable](Advent%20Of%20Cyber%2025/6-Malware-Analysis-Egg-xecutable.md)
    1. [Network Discovery - Scan-ta Clause](Advent%20Of%20Cyber%2025/7-Network-Discovery-Scan-ta-Clause.md)
    1. [Prompt Injection - Sched-yule conflict](8-Prompt-Injection-Sched-yule-conflict.md)
    1. [Passwords - A Cracking Christmas](9-Passwords-A-Cracking-Christmas.md)
    1. [SOC Alert Triaging - Tinsel Triage](10-SOC-Alert-Triaging-Tinsel-Triage.md)
    1. [XSS - Merry XSSMas](11-XSS-Merry-XSSMas.md)
    1. [Phishing - Phishmas Greetings](12-Phishing-Phishmas-Greetings.md)
    1. [YARA Rules - YARA mean one!](13-YARA-Rules-YARA-mean-one.md)
    1. [Containers - DoorDasher's Demise](14-Containers-DoorDashers-Demise.md)

# OpenVPN
## Get Connected
### Download the OpenVPN GUI open-source application.
- Arch Linux
    - [OpenVPN](https://wiki.archlinux.org/title/OpenVPN)
        - [qopenvpn](https://archlinux.org/packages/?name=qopenvpn)
        - [networkmanager-openvpn](https://archlinux.org/packages/?name=networkmanager-openvpn)

### Import the VPN configuration file
- [Download](https://tryhackme.com/access)

### Connecting
- Arch Linux
    - Download, `sudo pacman -Syu openvpn`
    - Connect, `sudo openvpn /path-to-file/file-name.ovpn`