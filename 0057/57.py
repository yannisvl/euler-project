# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:57:47 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

def num_digs(n):
    return math.floor(math.log(n, 10)) + 1

ti = time.time() 

a = 1
d = 1

total = 0
for i in range(1001):
    tempa = a
    tempd = d
    a = 2*tempd + tempa
    d = tempd + tempa
    if num_digs(a)>num_digs(d):
        total+=1
print(total)

print("time elapsed", time.time()-ti)