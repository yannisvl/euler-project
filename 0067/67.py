import numpy as np
f = open("./0067/p067_triangle.txt", "r")
l = []
for line in f:
    l.append(line.split(' '))
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])
a = np.zeros([100, 100])
for j in range(100):
    a[99, j] = l[99][j]
for i in range(98, -1, -1):
    for j in range(i+1):
        a[i][j] = np.max( (a[i+1][j], a[i+1][j+1]) ) + l[i][j]
print(a[0][0])


