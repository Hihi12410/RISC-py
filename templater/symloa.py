#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Load symbols.

from logutils import logger
from fio import futils as fu
import binutils.binutils as bu

# The logger.
log:logger.Logger = logger.Logger("symloa")

# Load symbol paths from path.
def __loa_sympaths(fpath:str)->list[list[str,str]]:
    try:
        return fu.__lfiles(fpath)
    except Exception as e:
        log.error_log(e.__str__())
        return [["", ""]]

# Load aarch symbols from path.
def __loa_sympaths(aarch_name:str, sympath_dirs:list[list[str, str]])->list[str, list[str,str]]:
    try:
        return [aarch_name, fu.__lfiles(sympath_dirs)]
    except Exception as e:
        log.error_log(e.__str__())
        return ["", ["", ""]]

# Expand __AARCH tables.
def __exp_aarch(aarch_symbols:list[str, list[str, str]])->list[str, bu.__AARCH, list[str,str]]:
    try:
        aarch_f = [f[1] for f in aarch_symbols[1] if f[0] == f"{aarch_symbols[0]}.aarch"][0]
        dat:str = ""
        with fu.__open_rb(aarch_f) as _f:
            dat = _f.read()
        return [aarch_symbols[0], bu.__parse_aarch(dat), aarch_symbols[1]]
    except Exception as e:
        log.error_log(e.__str__())
        return ["", bu.__AARCH, ["", ""]]

# Expand symbols.
def __exp_sym():
    NotImplemented