from datetime import datetime

import math

startt = datetime.now()
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


sum = 0
for i in range(2, 2000000):
    if is_prime(i): sum+=i
print(sum)
print (datetime.now() - startt)