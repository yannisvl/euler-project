# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:23:34 2020

@author: ΓΙΑΝΝΗΣ
"""

import math 

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

print(nCr(40,20))