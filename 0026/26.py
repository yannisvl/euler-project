# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:08:14 2020

@author: ΓΙΑΝΝΗΣ
"""

def fractionToDecimal(numr, denr):
     
    # Initialize result
    res = "" 
    mp = {}
    rem = numr % denr
  
    while ((rem != 0) and (rem not in mp)):
        
        mp[rem] = len(res)
         
        rem = rem * 10
  
        res_part = rem // denr #this is the actual part in the number
        res += str(res_part)
  
        rem = rem % denr #if the same remainder is found then break
     
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]
 
numr=1
mymax = -1
max_den=-1
for denr in range(2,1000):
    res = fractionToDecimal(numr, denr)
    print(denr)
    if (res == ""):
        print("No recurring sequence")
    else:
        print("Recurring sequence is", res)
        if len(res)>mymax:
            mymax=len(res)
            max_den=denr
print(max_den)