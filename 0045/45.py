# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:50:25 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def triangle():
    n=285
    num=n*(n+1)//2
    yield num
    while 1:
        num=n*(n+1)//2
        yield num
        n+=1

def pent(limit):
    s = []
    n=165
    num=n*(3*n-1)//2
    s.append(num)
    while num<limit:
        num=n*(3*n-1)//2
        s.append(num)
        n+=1
    return s

def hexagonal(limit):
    s = []
    n=165
    num=n*(2*n-1)
    s.append(num)
    while num<limit:
        num=n*(2*n-1)
        s.append(num)
        n+=1
    return s

lim = 10000000000
p = set(pent(lim))
h = set(hexagonal(lim))
g = triangle()
while True:
    a = next(g)
    if a in p and a in h:
        print(a)
        break

print("time elapsed", time.time()-ti)