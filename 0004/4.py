# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:06:48 2020

@author: ΓΙΑΝΝΗΣ
"""

def ispalindrome(n):
    return str(n)==str(n)[::-1]

mymax=-1
for i in range(100, 1000):
    for j in range(100, 1000):
        if ispalindrome(i*j) and mymax<i*j:
            mymax=i*j
print(mymax)