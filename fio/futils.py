#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Basic file utilities.

import logutils.logger as logger
from typing import Iterable, IO
from os import path, listdir

# Setup logging.
log:logger.Logger = logger.Logger("futils")

# Open file for binary writing.
def __open_wb(fpath:str)->IO:
    f:object = None
    try:
        f = open(path.abspath(fpath), "wb")
        log.log(f"Opened {fpath} for binary writing.")
    except Exception as e:
        log.error_log(e.__str__())
    return f

# Open file for binary reading.
def __open_rb(fpath:str)->IO:
    f:object = None
    try:
        f = open(path.abspath(fpath), "rb")
        log.log(f"Opened {fpath} for binary reading.")
    except Exception as e:
        log.error_log(e.__str__())
    return f

# NEVER FORGET TO CLOSE FILES!!!

# Write 8 bit symbols to file
def __wfb(f:IO, dat:Iterable[int]):
    try:
        f.write(bytes(dat))
    except Exception as e:
            log.error_log(e.__str__())

# Return directory listing of path.
def __ldirs(fpath:str)->list[str]:
    try:
        _p:str = path.abspath(fpath)
        return [[d, path.join(_p, d)] for d in listdir(_p) if path.isdir(path.join(_p, d))]
    except Exception as e:
        log.error_log(e.__str__())
        return [""]

# Return file listing of path.
def __lfiles(fpath:str)->list[str]:
    try:
        _p:str = path.abspath(fpath)
        return [[f, path.join(_p, f)] for f in listdir(_p) if path.isfile(path.join(_p, f))]
    except Exception as e:
        log.error_log(e.__str__())
        return [""]

