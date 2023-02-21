# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:29:07 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

per = np.zeros(2000, dtype=int)

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)
        
def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim


ti = time.time() 

g = gen_all_pyth_trips(500)

for i in g:
    per[np.sum(i)]+=1

print(np.argmax(per))
print(per[np.argmax(per)])

print("time elapsed", time.time()-ti)