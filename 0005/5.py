# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:10:37 2020

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



# for each prime number to 20, find the max exponent before reaching 20
l = SieveOfEratosthenes(20)
product = 1
for i in range(20):
    if l[i]==1:
        exponent = np.floor(np.log(20)/np.log(i)) #that's log 20 with base 2
        product*=i**exponent
print(product)