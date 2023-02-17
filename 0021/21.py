def sum_of_proper_divisors(n):
    arxikos = n
    product = 1
    ektheths = 0
    if n % 2 == 0:
        ektheths = 1
        n = n / 2
        while n % 2 == 0:
            ektheths += 1
            n = n / 2
        product = (2**(ektheths+1)-1)
    factor = 3
    while n > 1:
        if n % factor == 0:
            ektheths = 1
            n = n / factor
            while n % factor == 0:
                ektheths += 1
                n = n / factor
            product = product * (factor**(ektheths + 1) - 1) / (factor-1)
        factor += 2
        ektheths = 0
    return (product-arxikos)

list = []
limit = 10000
for i in range(1, limit):
    list.append(sum_of_proper_divisors(i))
j = 1
total_sum = 0
while j<limit :
    if list[j-1]<limit-1:
        if list[int(list[j-1])-1] == j and j != list[j-1]:
            print(j, list[j-1])
            total_sum+= j + list[j-1]
    j+=1
total_sum/= 2
print (total_sum)