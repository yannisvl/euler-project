# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:35:03 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def isPandigital(num):
	return len(num) == 9 and set(num) == set("0123456789")

mysum=0
for x in it.permutations('0123456789'):
    a = int(''.join(x))
    if int(x[3])%2!=0:
        continue
    if int(''.join(x[2:5]))%3!=0:
        continue
    if x[5]!='5':
        continue
    if int(''.join(x[4:7]))%7!=0:
        continue
    if int(''.join(x[5:8]))%11!=0:
        continue
    if int(''.join(x[6:9]))%13!=0:
        continue
    if int(''.join(x[7:10]))%17!=0:
        continue    
    mysum+=a

print(mysum)
print("time elapsed", time.time()-ti)