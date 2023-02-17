# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:07:30 2020

@author: ΓΙΑΝΝΗΣ
"""

import math

def num_digs(n):
    return math.floor(math.log(n, 10)) + 1

def fib():
    a, b = 0, 1
    yield 0
    yield 1
    while True:
        c = a+b
        a, b = b, c
        yield b
    
g = fib()
i=0
for x in g:
    if x>0 and num_digs(x)>999:
        print(i)
        break
    i+=1