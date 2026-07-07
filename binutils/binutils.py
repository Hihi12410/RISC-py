#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Binutils - Utilities for bit manipulation.

from __future__ import annotations
import functools
from typing import Final, Any, overload, TypeAlias, Callable
from enum import Enum
from logutils.logger import Logger as logger
import arith.arith as ar


# Global setup - Endianness and significance
class __ENDIANNESS_ENUM(Enum):
    BIG:int = 0x0
    LITTLE:int = 0x1

class __SIGNIFICANCE_ENUM(Enum):
    MSBZ:int = 0x2
    LSBZ:int = 0x3

# The WORD type.
WORD:TypeAlias = tuple[int, __SIGNIFICANCE_ENUM]

# __AARCH -> Endianness, Significance, Word size
__AARCH:TypeAlias = tuple[__ENDIANNESS_ENUM, __SIGNIFICANCE_ENUM, int]
# __CONFIG_T -> Host aarch, Target aarch
__CONFIG_T:TypeAlias = tuple[__AARCH, __AARCH]
__CONFIG:__CONFIG_T | None = None

# Global logger.
log:logger = None

# Initialize module
def init(host:__AARCH, target:__AARCH) -> None:
    
    global __CONFIG, log

    log = logger("BinUtils")
    if not host or not target:
        log.error_log("The initialization of BinUtils failed.")
        return
    __CONFIG = (host, target)
    log.init_log(f"{host} targeting {target}.")
    
# Assert module initialization.
def _assert_init(x:Callable)->Callable|None:
    @functools.wraps(x)
    def bypass(*args, **kwargs):
        if __CONFIG is None:
            log.error_log("Module is not initialized!")
            return None
        return x(*args, **kwargs)
    return bypass

# Bitwise operations

# Assert HOST's WORDSIZE size WORD.
@_assert_init
def __assert_wordsz(x:Any) -> int:
    return x & ar.__mask_range(0, __CONFIG[0][2]-1)

# Assert TARGET's WORDSIZE size WORD.
@_assert_init
def __assert_wordsz(x:Any) -> int:
    return x & ar.__mask_range(0, __CONFIG[1][2]-1)

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
                pass
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