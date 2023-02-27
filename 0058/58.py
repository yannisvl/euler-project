import numpy as np
import itertools as it
import math, time

ti = time.time() 

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

ratio = 1
length = 1
current_num = 1
step = 0
total_numbers_in_diagonals = 1
total_primes = 0

while ratio >= 0.1:
    length += 2
    step += 2
    total_numbers_in_diagonals += 4
    
    for i in range(4):
        current_num += step
        if isprime(current_num):
            total_primes += 1

    ratio = total_primes / total_numbers_in_diagonals
    

print(length)
print("time elapsed", time.time()-ti)