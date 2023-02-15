import time
start = time.time()
file = open("./0011/p011_pinakas.txt", "r")
a = []
for line in file:
    x = line.split(' ')
    a.append([int(x[i]) for i in range(20)])
file.close()
maxpro = 1

#horizontally
for i in range(20):
    temp = a[i][0]*a[i][1]*a[i][2]*a[i][3]
    if temp>maxpro:
        maxpro = temp
    for j in range(4, 20):
        if a[i][j]!=0:
            if a[i][j-4]!=0:
                temp = temp / a[i][j-4] * a[i][j]
            else:
                temp = a[i][j]*a[i][j-1]*a[i][j-2]*a[i][j-3]
        else :
            temp = 0
        if temp>maxpro:
            maxpro = temp

#vertically
for j in range(20):
    temp = a[0][j]*a[1][j]*a[2][j]*a[3][j]
    if temp>maxpro:
        maxpro = temp
    for i in range(4, 20):
        if a[i][j]!=0:
            if a[i-4][j]!=0:
                temp = temp / a[i-4][j] * a[i][j]
            else:
                temp = a[i][j]*a[i-1][j]*a[i-2][j]*a[i-3][j]
        else :
            temp = 0
        if temp>maxpro:
            maxpro = temp

#main diagonal
for i in range(17):
    for j in range(17):
        temp = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
        if temp>maxpro:
            maxpro = temp

#secondary diagonal
for i in range(16, 2, -1):
    for j in range(19, 2, -1):
        temp = a[i][j]*a[i+1][j-1]*a[i+2][j-2]*a[i+3][j-3]
        if temp>maxpro:
            maxpro = temp
            
print(maxpro)
end = time.time()
print(end - start, 'sec')