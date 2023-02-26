# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:11:32 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

my_max = -1
for a in range(100):
    for b in range(100):
        s = str(a**b)
        my_sum = sum([int(x) for x in s])
        my_max = max(my_sum, my_max)

print(my_max)
print("time elapsed", time.time()-ti)