import math

g = 2*3*5*7*11*13*17*19*23

def calculate_totient(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result


def calculate_resilience(n):
    totient = calculate_totient(n)
    return totient / (n - 1)

for i in range(1,10):
    if calculate_resilience(i*g) < 15499 / 94744:
        print(i*g) 
        break