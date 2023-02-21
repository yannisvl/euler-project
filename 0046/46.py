def isprime(n):
    if n < 0 :
        return False
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

squares = [1, 4, 9]
found = False
bash = 3
i = 9
while not found:
    if isprime(i):
        i+=2
    else :
        if i>squares[-1]:
            bash+=1
            squares.append(bash**2)
        j = 0
        isxuei = False
        while not isxuei and j<len(squares):
            if isprime(i - 2*squares[j]):
                isxuei = True
                print(i, "=", i-2*squares[j], "+ 2 * ", j, "^2")
            j+=1
        if j==len(squares):
            found = True
        i+=2
print(i-2)

