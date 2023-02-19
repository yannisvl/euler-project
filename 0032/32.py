# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:00:33 2020

@author: ΓΙΑΝΝΗΣ
"""

import itertools
import numpy as np

myset = set()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 0
for b in itertools.permutations(a):
    for (i, j) in [(1,4), (2,3)]:
            c1 = b[:i]
            c2 = b[i:i+j]
            c3 = b[i+j:]
            d1 = int(''.join(map(str,c1)))
            d2 = int(''.join(map(str,c2)))
            d3 = int(''.join(map(str,c3)))
            if d1*d2==d3:
                print(d1, d2, d3)
                myset.add(d3)
print(myset)
print(np.sum(list(myset)))