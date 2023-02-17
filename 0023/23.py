# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:14:38 2020

@author: ΓΙΑΝΝΗΣ
"""
import numpy as np

def sum_of_proper_divisors(n):
    arxikos = n
    product = 1
    ektheths = 0
    if n % 2 == 0:
        ektheths = 1
        n = n / 2
        while n % 2 == 0:
            ektheths += 1
            n = n / 2
        product = (2**(ektheths+1)-1)
    factor = 3
    while n > 1:
        if n % factor == 0:
            ektheths = 1
            n = n / factor
            while n % factor == 0:
                ektheths += 1
                n = n / factor
            product = product * (factor**(ektheths + 1) - 1) / (factor-1)
        factor += 2
        ektheths = 0
    return (product-arxikos)

s = set()
for i in range(12, 28124):
    if sum_of_proper_divisors(i)>i:
        s.add(i)
        
a = np.zeros(2*28125)
            
for i in s:
    for j in s:
        a[i+j] = 1
            
mysum = 0
for i in range(1, 28124):
    if a[i]==0:
        mysum+=i
print(mysum)