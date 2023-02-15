f = open("./0013/p013_100nums.txt", "r")
sum = 0
for line in f:
    x = int(line)
    sum += x
print(sum)
a = str(sum)
print(a[:10])
sumof =0
a = 2**1000
while a>0:
    sumof += a%10
    a//=10
print(sumof)