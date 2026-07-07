#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v.2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at https://mozilla.org/MPL/2.0/.

# Simple arithmetic utilities.

# Raise x to the power of y given y is a positive integer.
# Works.
def __pow_host_numerical(x:int, y:int)->int:
    z:int = 1
    while y > 0:
        z *= x
        y -= 1
    return z

# 2^n given x >= 0.
# Works.
def __host_pow2(x:int)->int:
    return (0x1<<x)

# Calculate bitmask of size n.
# Works.
def __mask(n:int)->int:
    return (1<<(n))-1

# Calculate bitmask. Range bit x to bit y. x <= y.
# Works.
def __mask_range(x:int, y:int)->int:
    hi_mask:int = __mask(y+1)
    lo_mask:int = __mask(x)
    return hi_mask-lo_mask

# Flip bit order of x given WORDSZ of wsz.
# Works.
def __flip(x:any, wsz:int)->int:
    x = x & __mask(wsz)
    y:int = 0x0
    for i in range(0, wsz):
        y |= (((x&__host_pow2(i))>>i)<<(wsz-i-1))
    return y