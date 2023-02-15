def num_divisors(n):
    product = 1
    ektheths = 0
    if n%2==0 :
        ektheths = 1
        n = n / 2
        while n%2==0 :
            ektheths+=1
            n = n / 2
        product = product * (ektheths + 1)
    factor = 3
    while n>1 :
        if n%factor == 0 :
            ektheths=1
            n = n / factor
            while n%factor == 0 :
                ektheths+=1
                n = n / factor
            product = product * (ektheths + 1)
        factor+=2
        ektheths = 0
    return product


i = 32
tr = i*(1+i)/2
while num_divisors(tr)<=500 :
    i+=1
    tr = i*(i+1)/2
print(tr)