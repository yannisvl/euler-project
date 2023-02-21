# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:29:37 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def td_factors(n, limit=1000000):
    if type(n) != int:
        raise TypeError("must be integer")
    fs = []
    lastf=1
    if n%2==0:
        lastf=2
        fs += [2]
        while n % 2 == 0:
            n /= 2
    if n == 1:
        return fs
    f = 3
    while f * f <= n:
        if limit < f:
            raise OverflowError("limit exceeded")
        if n % f == 0:
            if f!=lastf:
                fs += [f]
            lastf = f
            n /= f
        else:
            f += 2
        if len(fs)>4:
            return fs
    return fs+[n]

i = 644
while 1:
    if len(td_factors(i))==len(td_factors(i+1))==len(td_factors(i+2))==len(td_factors(i+3))==4:
        print(i)
        break
    i+=1

print("time elapsed", time.time()-ti)