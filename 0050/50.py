# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:27:09 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def SieveOfEratosthenes(n): 
    prime = np.ones(n+1, dtype=bool)
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return np.where(prime==True)[0]


def is_prime(n):
    if type(n) != int:
        raise TypeError("must be integer")
    if n < 2:
        return False
    ps = [2,3,5,7,11,13,17,19,23,29,31,37,41,
          43,47,53,59,61,67,71,73,79,83,89,97]
    def is_spsp(n, a):
        d, s = n-1, 0
        while d%2 == 0:
            d /= 2; s += 1
        t = pow(int(a),int(d),int(n))
        if t == 1:
            return True
        while s > 0:
            if t == n-1:
                return True
            t = (t*t) % n
            s -= 1
        return False
    if n in ps: return True
    for p in ps:
        if not is_spsp(n,p):
            return False
    return True


l = sorted(set(SieveOfEratosthenes(10000)))

maxnum = -1
maxm = -1
for m in range(21, 1000):
    mysum = np.sum(l[:m])
    
    if is_prime(int(mysum)) and mysum<1000000:
        maxnum=mysum
        maxm = m
    for i in range(1, len(l)-m-1):
        mysum = mysum - l[i-1] + l[i+m-1]
        if is_prime(int(mysum)) and mysum<1000000:
            maxnum=mysum
            maxm = m
                
print(maxnum, maxm)

print("time elapsed", time.time()-ti)