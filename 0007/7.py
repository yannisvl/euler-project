# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:23:35 2020

@author: ΓΙΑΝΝΗΣ
"""
import numpy as np

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
    return prime

l = SieveOfEratosthenes(150000)
count=0
for i in range(150000):
    if l[i]==1:
        count+=1
        if count==10001:
            print(i)
            break
