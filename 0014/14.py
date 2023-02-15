already = {}

i = 1
max = 0
maxi = 0
while i<1000000 :
    temp = i
    chain = 1
    while temp!=1:
        if temp%2==0:
            temp/=2
        else :
            temp = 3*temp + 1
        if temp in already:
            chain+=already[temp]
            break
        else:
            chain+=1
    already[i] = chain
    
    if chain>max :
        max = chain
        maxi = i
    i+=1
print(maxi, max)

