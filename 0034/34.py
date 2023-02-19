# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:40:46 2020

@author: ΓΙΑΝΝΗΣ
"""

import math
import numpy as np

total=0
for i in range(3, 1000000):
    s = list(map(int, str(i)))
    k = np.sum(list(map(math.factorial, s)))
    if k==i:
        print(i)
        total+=k 
print(total)