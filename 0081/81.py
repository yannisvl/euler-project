import numpy as np
f = open("./0081/p081_matrix.txt", "r")
array80 = []
mindist = np.zeros([80, 80])
for line in f :
    array80.append([int(x) for x in line.split(',')])
mindist[0, 0] = array80[0][0]
for j in range(1, 80):
    mindist[0, j] = mindist[0, j-1] + array80[0][j]
for i in range(1, 80):
    mindist[i, 0] = mindist[i-1, 0] + array80[i][0]
    for j in range(1, 80):
        mindist[i, j] = min(mindist[i, j-1], mindist[i-1, j]) + array80[i][j]
print(mindist[79,79])
f.close()