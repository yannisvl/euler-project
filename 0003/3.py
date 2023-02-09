n = 600851475143

i = 3
largest=1
while n > 1 :
    while n%i==0:
        n /= i
        largest = i
    i+=2
print(largest)
