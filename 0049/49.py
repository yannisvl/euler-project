# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:08:51 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def primes(n):
    if type(n) != int:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    m = (n-1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i += 1; p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1; p += 2
    return ps


a = sorted(set(primes(10000)) - set(primes(1000)))

found=False
for i in a:
    k=0
    for j in it.permutations(str(i)):
        jj = int(''.join(j))
        if jj in a:
            if jj!=i:
                if k==0:
                    second=jj
                    k=1
                elif k==1:
                    if jj!=second:
                        third=jj
                        nums = sorted([i, second, third])
                        #print(nums)
                        if second-i==third-second:
                            found = True
                            print(nums)
                            break
                    
    if found:
        break
 
nums = [i, second, third]
s = ''.join(map(str,sorted(nums)))
print(s)    

print("time elapsed", time.time()-ti)