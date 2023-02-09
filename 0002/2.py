# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:44:47 2020

@author: ΓΙΑΝΝΗΣ
"""

def fib():
    a, b = 0, 1
    mysum=0
    while b<=4000000:
        c = a+b
        if c%2==0: mysum+=c
        a, b = b, c
    print(mysum)

fib()