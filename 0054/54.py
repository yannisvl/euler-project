# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:56:19 2020

@author: ΓΙΑΝΝΗΣ
"""

import numpy as np
import itertools as it
import math, time

ti = time.time() 

def get_counts(l):
    c = np.zeros(15)
    for x in l:
        c[x] += 1    
    return c

def check(a, b):
    straight = False
    royal = False
    flush = False
    high = max(a)
    
    if a[0]==a[1]-1==a[2]-2==a[3]-3==a[4]-4:
        straight = True
        if a[4]==13:
            royal = True
    if a[0]==a[1]-1==a[2]-2==a[3]-3==2 and a[4]==14:
        straight= True
    if len(set(b))==1:
        flush = True
    cnts = get_counts(a)
    print(cnts)
    threes = 3 in cnts
    fours = 4 in cnts
    twos = np.count_nonzero(cnts==2)
    return high, twos, threes, fours, straight, royal, flush

def score(a, b):
    high, twos, threes, fours, straight, royal, flush = check(a, b)
    if flush and royal:
        print("royal flush")
        return 10
    elif straight and flush:
        print("straight flush")
        return 9
    elif fours:
        print("fours")
        return 8
    elif threes and twos:
        print("full house")
        return 7
    elif flush:
        print("flush")
        return 6
    elif straight:
        print("straight")
        return 5
    elif threes:
        print("threes")
        return 4
    elif twos==2:
        print("2 pairs")
        return 3
    elif twos:
        print("1 pair")
        return 2
    else:
        print("high")
        return 1
    
    
def eval_tie(x, y, level):
    if level==1:
       for (x1,y1) in zip(reversed(x), reversed(y)):
           if x1!=y1:
               return (x1, y1)
    elif level==2:
        cnts1 = get_counts(x)
        k1 = np.where(cnts1==2)[0][0]
        cnts2 = get_counts(y)
        k2 = np.where(cnts2==2)[0][0]
        if k1!=k2:
            return (k1, k2)
        else:
            return (max(set(x) - {k1}), max(set(y)- {k1}))
    elif level==3:
        cnts1 = get_counts(x)
        k1 = np.where(cnts1==2)[0]
        cnts2 = get_counts(y)
        k2 = np.where(cnts2==2)[0]
        if max(k1) != max(k2):
            return (max(k1), max(k2))
        elif min(k1) != min(k2):
            return (min(k1), min(k2))
        else:
            return (max(set(x)-set(k1)), max(set(y)-set(k2)))
    elif level==4:
        cnts1 = get_counts(x)
        k1 = np.where(cnts1==3)[0][0]
        cnts2 = get_counts(y)
        k2 = np.where(cnts2==3)[0][0]
        if k1!=k2:
            return (k1, k2)
        else:
            return (max(set(x)-{k1}), max(set(y) - {k2}))
    elif level==5:
        return(x[0], y[0])
    elif level==6:
        cnts1 = get_counts(x)
        cnts2 = get_counts(y)
        if 3 in cnts1 and 3 in cnts2:
            return eval_tie(x, y, 4)
        elif np.count_nonzero(cnts1==2)==np.count_nonzero(cnts2==2)==2:
            return eval_tie(x,y,3)
        elif 2 in cnts1 and 2 in cnts2:
            return eval_tie(x,y,2)
        else:
            return eval_tie(x,y,1)
    elif level==7:
        cnts1 = get_counts(x)
        k11 = np.where(cnts1==3)[0][0]
        k12 = np.where(cnts1==2)[0][0]
        cnts2 = get_counts(y)
        k21 = np.where(cnts2==3)[0][0]
        k22 = np.where(cnts2==2)[0][0]
        if k11!=k21:
            return k11, k21
        else:
            return k12, k22
    elif level==8:
        cnts1 = get_counts(x)
        k11 = np.where(cnts1==4)[0][0]
        k12 = np.where(cnts1==1)[0][0]
        cnts2 = get_counts(y)
        k21 = np.where(cnts2==4)[0][0]
        k22 = np.where(cnts2==1)[0][0]
        if k11!=k21:
            return k11, k21
        else:
            return k12, k22
    elif level==9:
        return(x[0], y[0])
        
           
    
    
    
def winner1(p1, p2):
    a1 = [x for (x,_) in p1]
    b1 = [x for (_, x) in p1]
    a2 = [x for (x,_) in p2]
    b2 = [x for (_, x) in p2]
    s1 = score(a1, b1)
    s2 = score(a2, b2)
    if s1 > s2:
        return 1
    elif s1 < s2:
        return 0
    else:
        print("we have a tie")
        tie1, tie2 = eval_tie(a1, a2, s1)
        if (tie1 > tie2):
            return 1
        else:
            return 0

l = [hands.strip('\n').split(' ') for hands in open("./0054/p054_poker.txt", 'r').readlines()]
total=0

i = 0
for hand in l:
    p1_n=[]
    p2_n=[]
    p1_s=[]
    p2_s=[]
    for s in hand[:5]:
        if s[0].isdigit():
            p1_n.append(int(s[0]))
        elif s[0]=='T':
            p1_n.append(10)
        elif s[0]=='J':
            p1_n.append(11)
        elif s[0]=='Q':
            p1_n.append(12)
        elif s[0]=='K':
            p1_n.append(13)
        elif s[0]=='A':
            p1_n.append(14)
        p1_s.append(s[1])
    for s in hand[5:]:
        if s[0].isdigit():
            p2_n.append(int(s[0]))
        elif s[0]=='T':
            p2_n.append(10)
        elif s[0]=='J':
            p2_n.append(11)
        elif s[0]=='Q':
            p2_n.append(12)
        elif s[0]=='K':
            p2_n.append(13)
        elif s[0]=='A':
            p2_n.append(14)
        p2_s.append(s[1])  
    if i>=0 and i<=1000:
        p1 = sorted(zip(p1_n, p1_s))
        p2 = sorted(zip(p2_n, p2_s))
        print(p1, p2)
        result = winner1(p1,p2)
        print("winner is", 2-result)
        total+=result
        print()
    i+=1
print(total , '/', len(l))

print("time elapsed", time.time()-ti)