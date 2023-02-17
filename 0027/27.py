# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:09:09 2020

@author: ΓΙΑΝΝΗΣ
"""

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

mymax = -1
amax = 0
bmax = 0
for a in range(-999, 1000):
    for b in range(-1000, 1000):
        n=0
        while isprime(n**2 + a*n + b):
            n+=1
        if n>mymax:
            mymax=n
            amax=a
            bmax=b
print(amax*bmax, mymax)
            
            