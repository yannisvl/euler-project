a = [[1], [1, 1]]
sum = 0
for i in range(2, 101):
    print(i)
    a.append([1])
    for j in range(1, i):
        a[i].append( a[i-1][j-1] + a[i-1][j] )
        if a[i][j]>1000000:
            sum+=1
            print(i, j, a[i][j])
    a[i].append(1)
print(sum)