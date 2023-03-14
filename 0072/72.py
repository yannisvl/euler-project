from fractions import Fraction
import math

def totient(n):
    pr = n
    if n%2==0:
        pr /= 2
        while n%2==0:
            n/=2
    upopshfio = 3
    while n!=1:
        if n%upopshfio==0:
            pr/=upopshfio
            pr*=upopshfio-1
            while n%upopshfio==0:
                n/=upopshfio
        upopshfio+=2
    return pr

f = [0, 1, 1, 2]

def totient_function(n):
    if n%2==0:
        if (n//2)%2==0:
            f.append(2*f[n//2])
        else :
            f.append(f[n//2])
        return f[n]
    else :
        i = 3
        temp = n
        while i< math.floor(math.sqrt(temp))+2:
            if n%i==0:
                times =0
                while n%i==0:
                    times+=1
                    n//=i
                if n==1:
                    f.append(temp-temp/i)
                    return f[temp]
                else:
                    f.append(f[i**times]*f[n])
                    return f[temp]
            i+=2
        f.append(temp-1)
        return temp-1

sum = 3

# equivalently, we are looking for each denominator i, the numbers relative to it
for i in range(4, 1000001):
    sum+=totient_function(i)
print(sum)
print('72 finished')