# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:01:01 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def pentagonal(limit):
    n=1
    a = set()
    num=0
    while num<limit:
        num = n*(3*n-1)//2
        a.add(num)
        n+=1
    return a

lim=100000000
b = pentagonal(lim)
pent = sorted(b)

mymin = 1000000000000
for i in range(len(pent)):
    x=pent[i]
    for j in range(i):
        y=pent[j]
        if x-y in b and x+y in b and np.abs(x-y)<mymin:
            mymin = np.abs(x-y)
print(mymin)

print("time elapsed", time.time()-ti)