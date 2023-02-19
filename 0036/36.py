def is_palindrome(n):
    s = str(n)
    return s[0:len(s):1] == s[::-1]

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

def binary(n):
    l = []
    while n>0:
        l = [n%2] + l
        n=n//2
    return magic(l)

sum = 0
i = 1
while i<1000000:
    if is_palindrome(i):
        if is_palindrome(binary(i)):
            sum+=i
            print(i, binary(i))
    i+=1
print (sum)


