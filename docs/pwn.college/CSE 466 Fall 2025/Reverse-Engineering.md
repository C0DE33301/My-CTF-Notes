---
layout: default
title: Reverse Engineering
parent: CSE 466 Fall 2025
nav_order: 1
---

# Notes
### Intro
- Compilation process loss
    - Comments
    - Variable names
    - Function names
### Data Access
### Static tools
- Tools
    - `kaitai struct`, 
    - `nm`, 
    - `strings`, Dumps ASCII strings found in the file.
    - `objdump`, 
    - `checksec`, 
- Advanced Disassemblers
    - `IDA Pro`, Interactive Disassembler
    - `Binary Ninja`
    - `Binary Ninja Cloud`, Runs on browsers, ...
    - `angr management`
    - `ghidra`
    - `cutter`

# Challenges
- [Crackme](#crackme)
    - [Terrible Token (Easy)](#terrible-token-easy)
    - [Terrible Token (Hard)](#terrible-token-hard)

## Crackme
### Terrible Token (Easy)
Note: Find the correct license key
- File, `/challenge/terrible-token-easy`
- Trying, `checksec` command, ...
    ```
    [*] '/challenge/terrible-token-easy'
        Arch:       amd64-64-little
        RELRO:      Full RELRO
        Stack:      No canary found
        NX:         NX enabled
        PIE:        PIE enabled
        SHSTK:      Enabled
        IBT:        Enabled
        Stripped:   No
    ```
- Trying, `strings` command
- Found string, Example: `yxfuc`
- Run file, `/challenge/terrible-token-easy`
- Use found string & prints flag!
### Terrible Token (Hard)
Note: Find the correct license key
- File, `/challenge/terrible-token-hard`
- Trying, `checksec` command, ...
- Trying, `strings` command
- Found string, Example: `umjpc`
- Run file, `/challenge/terrible-token-hard`
- Run file, `/challenge/terrible-token-easy`
- Use found string & prints flag!