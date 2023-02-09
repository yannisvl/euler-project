# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:28:21 2020

@author: ΓΙΑΝΝΗΣ
"""
s=1000
for a in range(3,(s-3)//3):
    for b in range(a+1,(s-1-a)//2):
        c=s-a-b
        if c*c==a*a+b*b:
            print(a*b*c)