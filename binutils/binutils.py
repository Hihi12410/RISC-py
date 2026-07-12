#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Binutils - Utilities for bit manipulation.

from __future__ import annotations
import functools
from typing import Final, Any, overload, TypeAlias, Callable
from enum import Enum
import logutils.logger as logger
import arith.arith as ar


# Global setup - Endianness and significance
class __ENDIANNESS_ENUM(Enum):
    LSB:int = 0x0
    MSB:int = 0x1

class __SIGNIFICANCE_ENUM(Enum):
    LSBiZ:int = 0x0
    MSBiZ:int = 0x1

# The WORD type.
WORD:TypeAlias = tuple[int, __SIGNIFICANCE_ENUM]

# __ARCH -> Endianness, Significance, Word size
__ARCH:TypeAlias = tuple[__ENDIANNESS_ENUM, __SIGNIFICANCE_ENUM, int]

# Global logger.
log:logger.Logger = logger.Logger("binutils")

# Parse _ARCH parameters.
# example ::: <0, 2, 32>
def __parse_arch(s:str)->__ARCH:
    try:
        dat:list[str] = s.split('<')[1].split('>')[0].split(',')
        print(dat)
        return __ARCH((int(dat[0].strip()), int(dat[1].strip()), int(dat[2].strip())))

    except Exception as e:
        log.error_log(e.__str__())
        return __ARCH


# Assert AARCH's WORDSIZE size WORD.
def __assert_wordsz(x:Any, aarch:__ARCH) -> int:
    return x & ar.__mask_range(0, aarch[2]-1)