from itertools import product

def magic(numList):
    return int(''.join(map(str, numList)))

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def fromleft(i):
    cond = True
    s = ""
    for j in i:
       s+=j
       if not isprime(int(s)):
           cond=False
           break
    return cond


def fromright(i):
    cond = True
    s = ""
    for j in reversed(i):
       s=j+s
       if not isprime(int(s)):
           cond=False
           break
    return cond
        
        
mysum=0
total=0
r=1

while total<11:
    r+=1
    for i in product(['1','2','3','4','5','6','7','8','9','0'], repeat=r):
        #print(i)
        if fromleft(i) and fromright(i):
            num=magic(i)
            print(num)
            total+=1
            mysum+=num
print(mysum)