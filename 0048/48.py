def modpower(a,n):
    res=1
    while (n>0):
        if (n%2==1):
            res=res*a % 10000000000
        n//=2
        a=a*a % 10000000000
    return res

total = 0
for i in range(1, 1001):
    total += modpower(i, i)
    total%=10000000000
print(total)