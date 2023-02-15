# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:36:09 2020

@author: ΓΙΑΝΝΗΣ
"""
import numpy as np

f = open("./0018/p018_triangle.txt", "r")
l = []
for line in f:
    l.append(line.split(' '))
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])
a = np.zeros([15, 15], dtype=int)

#dynamic programming
for j in range(15):
    a[14, j] = l[14][j]
for i in range(13, -1, -1):
    for j in range(i+1):
        a[i,j] = np.max( (a[i+1,j], a[i+1,j+1]) ) + l[i][j]
print(a[0,0])