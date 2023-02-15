monades = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
dekades = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
eksairesh = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
ekatontades = []
ekatontades = [] + monades
for i in range(1, 10):
    ekatontades[i]+=10
sum = 0
for i in range(1, 1000):
    temp = sum
    decimal = (i//10)%10
    if decimal == 1 :
        sum+= eksairesh[i%10] + ekatontades[i//100]
    else :
        sum+= monades[i%10] + dekades[decimal] + ekatontades[i//100]
    if i%10==0 and decimal==0 : sum-=3
    print(i, sum-temp, i//100, decimal, i%10)
print(sum + 11)
print (monades, ekatontades)