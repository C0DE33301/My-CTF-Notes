---
layout: default
title: Ready Gladiator 1
parent: Medium
nav_order: 6
---

Files
- `imp.red`
    ```
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 1
    end
    ```
    - Written in Redcode, `;redcode`
    - The name of the program, `;name Imp Ex`
    - , `;assert 1`
    - Moves address 0 to address 1, `mov 0, 1`
    - End of program, `end`

Tips
- [Corewars for dummies](http://www.koth.org/info/corewars_for_dummies/dummies.html)
- [Corewars Online Play](https://crypto.stanford.edu/~blynn/play/redcode.html)

**Goal: Your warrior (warrior 1) must win at least once.**

Code
```as
;redcode
;name Imp Ex
;assert 1

jmp 4         ; **Jump**, Jumps to address 4
mov 2, -1     ; **Move**, Moves address 2 to address -1, invalid address?
jmp -1        ; **Jump**, Jump to address -1, Create a loop?
dat 9         ; **Data**, 
spl -2        ; **Split**, Creates 

end
```