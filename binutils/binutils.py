# Binutils - Utilities for bit manipulation.
import functools
from __future__ import annotations
from typing import Final, Any, overload, TypeAlias, Callable
from enum import Enum
from logging.logger import Logger


# Global setup - Endianness and significance
class __ENDIANNESS_ENUM(Enum):
    BIG:int = 0x0
    LITTLE:int = 0x1

class __SIGNIFICANCE_ENUM(Enum):
    MSBZ:int = 0x2
    LSBZ:int = 0x3

# __AARCH -> Endianness, Significance, Word size
__AARCH:TypeAlias = tuple[__ENDIANNESS_ENUM, __SIGNIFICANCE_ENUM, int]
# __CONFIG_T -> Host aarch, Target aarch
__CONFIG_T:TypeAlias = tuple[__AARCH, __AARCH]
__CONFIG:__CONFIG_T | None = None

# Initialize module
def init(host:__AARCH, target:__AARCH) -> None:
    Logger.init("BinUtils")
    if not host or not target:
        Logger.error_log("The initialization of BinUtils failed.")
        return
    __CONFIG = (host, target)
    Logger.init_log(f"{host} targeting {target}.")
    
# Assert module initialization.
def __assert_init(x:Callable)->Callable|None:
    @functools.wraps(x)
    def bypass(*args, **kwargs):
        if __CONFIG is None:
            Logger.error_log("Module is not initialized!")
            return None
        return x(*args, **kwargs)
    return bypass

# Bitwise operations lib.
class __bwops:
    # Get first x bits of WORD from HOST format to HOST format..
    @staticmethod
    @__assert_init
    def __gfb_host_tohost(x:Any, y:int):
        if __CONFIG[0][0] == __SIGNIFICANCE_ENUM.LSBZ:



        

        


# WORD core functions.
class __word_core:
    @overload
    @staticmethod
    def __new__WORD(_, w:WORD, value:int)->WORD:...
    @overload
    @staticmethod
    def __new__WORD(_, w:WORD, value:str)->WORD:...
    @overload
    @staticmethod
    def __new__WORD(_, w:WORD, value:tuple[int, ...])->WORD:...
    @overload
    @staticmethod
    def __new__WORD(_, w:WORD, value:tuple[str, ...])->WORD:...
    @staticmethod
    def __init__WORD(_, w:WORD, value:int|str|tuple[int,...]|tuple[str,...]=0x0)->WORD:
        match value:
            case int(x):
                
            case str(s):
                pass
            case tuple() as t:
                match t[0]:
                    case int(y):
                        pass
                    case str(z):
                        pass


    @staticmethod
    def __new_WORD(_, x:WORD, y:int):
        pass
    @staticmethod
    def __parse_int(_, x:int, )->int:
        return ()

# Word object - 8 bits.
class WORD:
    # Setup
    
            