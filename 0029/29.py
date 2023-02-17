# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:23:06 2020

@author: ΓΙΑΝΝΗΣ
"""
s = set()

for i in range(2, 101):
    for j in range(2,101):
        s.add(i**j)
print(len(s))