# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:38:33 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def get_counts(n):
    c = np.zeros(10)
    while n>0:
        c[n%10]+=1
        n//=10
    return c

found = False
a = 10
b = 16
while not found:
    for n in range(a, b+1):
        occs = get_counts(n)
        didntfind = False
        for i in range(2,7):
            if np.array_equal(occs, get_counts(n*i)):
                continue
            else:
                didntfind = True
                break
            
        if not didntfind:
            print(n)
            found=True
            break
    a*=10
    b = b*10 + 6
    
print("time elapsed", time.time()-ti)