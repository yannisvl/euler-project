# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:01:25 2020

@author: ΓΙΑΝΝΗΣ
"""

#check until when
for x in range(1, 20):
    print(x, int(x*'9')>x*9**5)
    
total=0
for i in range(2, 999999):
    s = str(i)
    fifths = sum([int(x)**5 for x in list(s)])
    if fifths == i :
        print(i)
        total+=i
        
print(total)