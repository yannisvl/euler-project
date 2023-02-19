def cyclic(a):
    n = len(a)
    return [[a[i - j] for i in range(n)] for j in range(n)]

def isprime(n):
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def is_circular(n):
    array = []
    while n>0:
        a = n%10
        if a%2==0:
            return False
        array.append(a)
        n=n//10
    einai =True
    for matrix in cyclic(array):
        arithmos = 0
        for j in range(len(matrix)):
            arithmos+=matrix[len(matrix)-1-j]*(10**j)
        if not isprime(arithmos):
            einai = False
            break
    return einai


sum = 1
i = 3
while i<1000000:
    if is_circular(i):
        sum+=1
        print(i)
    i+=2
print(sum)