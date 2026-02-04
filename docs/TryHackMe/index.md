---
title: TryHackMe
layout: default
---

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

# Command references
## gobuster
- **Find folders/files**
    - `gobuster dir --url <> -w /usr/share/wordlists/dirb/big.txt`
    - `gobuster dir --url <> -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt`
- **Find Subdomains**
    - `gobuster vhost -u 10.82.182.96 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain`
## Basic HTTP Server
- `nc -nlvp 80`
- `python3 -m http.server 80`
## Privilege Escalation
- **Sudo Privileges**, `sudo -l`
- **Group Privileges**

    |Group|Info|
    |---|---|
    |adm|Read access to log files, `/var/log`|
    - `id`
    - `find / -group <GROUP-NAME>`