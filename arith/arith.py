#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Simple arithmetic utilities.

# Raise x to the power of y given y is a positive integer.
def __pow_host_numerical(x:int, y:int)->int:
    z:int = 1
    while y > 0:
        z *= x
        y -= 1
    return z

# Calculate bitmask of size n.
def __mask(n:int)->int:
    return (1<<(n))-1

# Calculate bitmask. Range bit x to bit y. x <= y.
def __mask_range(x:int, y:int)->int:
    hi_mask:int = __mask(y+1)
    lo_mask:int = __mask(x)
    return hi_mask-lo_mask
