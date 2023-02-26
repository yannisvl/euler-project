import itertools as it
import math
import numpy as np

def is_prime(n):
    if type(n) != int:
        raise TypeError("must be integer")
    if n < 2:
        return False
    ps = [2,3,5,7,11,13,17,19,23,29,31,37,41,
          43,47,53,59,61,67,71,73,79,83,89,97]
    def is_spsp(n, a):
        d, s = n-1, 0
        while d%2 == 0:
            d /= 2; s += 1
        t = pow(int(a),int(d),int(n))
        if t == 1:
            return True
        while s > 0:
            if t == n-1:
                return True
            t = (t*t) % n
            s -= 1
        return False
    if n in ps: return True
    for p in ps:
        if not is_spsp(n,p):
            return False
    return True

def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p


def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def solve():

    primes = primes2(10000000)

    for p in primes:
        s = str(p)
        for j in set(s):
            if s.count(j)==3:
                total = 0
                l=[]
                for i in range(10):
                    t = s.replace(j, str(i))
                    if is_prime(int(t)) and len(s)==len(str(int(t))):
                        total+=1
                        l.append(t)   
                if total>=8:
                    print(s)
                    print(l)
                    return

         
if __name__ == '__main__':
    solve()              