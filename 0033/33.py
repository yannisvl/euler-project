# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:06:57 2020

@author: ΓΙΑΝΝΗΣ
"""

def simplify_fraction(a,b):
    c = 2
    while c<60:
        while a%c==0 and b%c==0:
            a, b = a//c, b//c
        c+=1
    return a,b


def funny_simplify(a,b):
    a0 = a%10
    a1 = a//10
    b0 = b%10
    b1 = b//10
    if a0==b0:
        if a0==0:
            return True, (a1, b1)
        else:
            return False, (a1, b1)
    elif a1==b1:
        return False, (a0, b0)
    
    if a0==b1:
        if a1==b0:
            return False, (1,1)
        else :
            return False, (a1,b0)
    elif a1==b0:
        if a0==b1:
            return False, (1,1)
        else :
            return False, (a0,b1)
    return True, (a,b)        

prod = 1
for d in range(10, 100):
    for n in range(10, d):
        #print(n,d)
        p1 = simplify_fraction(n,d)
        triv, p2 = funny_simplify(n,d)
        if p1==p2 and not triv:
            print((n,d),p1)
            prod*=p1[1]
print(prod)