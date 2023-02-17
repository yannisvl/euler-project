import itertools

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for b in itertools.permutations(a):
    sum+=1
    if sum==1000000:
        number = 0
        for i in range(10):
            number+=b[i]*(10**(9-i))
        break
print (number)