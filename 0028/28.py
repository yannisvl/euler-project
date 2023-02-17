# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:20:52 2020

@author: ΓΙΑΝΝΗΣ
"""
s = 1
number=1
gap = 2
for i in range(3,1002,2):
    for j in range(4):
        number+=gap
        s+=number
    gap+=2
print(s)