#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

import arith.arith as ar

# Integer to character.
# Works.
def itoc(x:int)->chr:
    return chr((x%10)+0x30)

# Render binary in tuple[int] format
# Works.
def render_bin(x:str, wsz:int):
    s:str = "0b"
    for i in range(0, wsz):
        s += itoc((x >> wsz-i-1) & 0x1)
    return s

# Render binary in hex format.
# TODO

__hext:tuple[chr, ...] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

# Number to hexchar.

def itohc(x:int)->chr:
    return __hext[x%16]

# Works.
def render_hex(x:str, wsz:int):
    s:str = "0x"
    rem = wsz % 4
    if rem != 0:
        s+=itohc((x >> wsz-rem)&ar.__mask(rem))
    i = wsz - rem
    while i > 3:
        i-=4
        s += itohc((x >> i) & ar.__mask(4))
    return s

# Logging module.
# Works.
class Logger:

    # Initialize module.
    def __init__(self, module_name:str)->None:
        self.__setattr__("name", module_name)
    
    # Log output
    def log(self, x:str):
        print(f"[ LOG  ] >> [ {self.__getattribute__("name")} ] >> {x}")
    
    # Log module loading.
    def init_log(self, x:str=""):
        print(f"[ INIT ] >> [ {self.__getattribute__("name")} ] >> {x if x else "SUCCESS"}")
    
    # Log module error.
    def error_log(self, x:str):
        print(f"[ ERR  ] >> [ {self.__getattribute__("name")} ] >> {x}")
    
    # Log module warnings.
    def warn_log(self, x:str):
        print(f"[ WARN ] >> [ {self.__getattribute__("name")} ] >> {x}")
    
    # Log module terminating.
    def quit_log(self, x:str):
        print(f"[ QUIT ] >> [ {self.__getattribute__("name")} ] >> {x}")