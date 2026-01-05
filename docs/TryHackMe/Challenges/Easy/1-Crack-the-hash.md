---
layout: default
title: Crack the hash
parent: Easy
nav_order: 1
---

# Crack the hash

## Notes

## Task 1 | 
### Question 1
```
48bb6e862e54f2a795ffc4e541caed4d
```
### Question 2
```
CBFDAC6008F9CAB4083784CBD1874F76618D2A97 
```
### Question 3
```
1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
```
### Question 4
```
$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
```
- Word, `bleh`
- Type, `3200 (bcrypt $2*$, Blowfish (Unix))`
1. `awk 'length < 5' /usr/share/wordlists/rockyou.txt | tee rockyou2.txt`
1. `hashcat -m 3200 pass.hash rockyou2.txt`
### Question 5
```
279412f945939ba78ce0758d3fd83daa
```

## Task 2 | 
### Question 1
```
F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
```
### Question 2
```
1DFECA0C002AE40B8619ECF94819CC1B
```
### Question 3
```
$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.
```
1. Word, `waka99`
1. Type, `1800 (sha512crypt $6$, SHA512 (Unix))`
- `awk 'length < 7' /usr/share/wordlists/rockyou.txt | tee rockyou3.txt`
- `hashcat -m 1800 pass.hash rockyou3.txt --force`
### Question 4
```
e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme
```