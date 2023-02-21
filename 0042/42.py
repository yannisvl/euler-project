# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:11:46 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

f = open("0042/p042_words.txt", "r")
l = [x.strip('"') for x in f.read().split(',')]

triangles = set()
i=1
while i<max([len(x) for x in l])*26:
    triangles.add(i*(i+1)//2)
    i+=1
    
total=0
for word in l:
    mysum = np.sum([ord(x)-64 for x in word])
    if mysum in triangles:
        total+=1
        
print(total)
print("time elapsed", time.time()-ti)