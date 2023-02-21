import itertools

def isprime(n):

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


for n in range(1, 10):
    for metablhth in itertools.permutations(range(1, n+1)):
        number = 0
        for i in range(n):
            number += metablhth[i] * (10 ** (n-1 - i))
        if isprime(number):
            print(number)

