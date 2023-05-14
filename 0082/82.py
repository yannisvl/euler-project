import numpy as np
f = open("./0082/p082_matrix.txt", "r")

n = 80

array80 = []
mindist = np.zeros([n, n])
for line in f :
    array80.append([int(x) for x in line.split(',')])

# array80 = [[131,673,234,103,18],[201,96,342,965, 150],
#            [630, 803, 746, 422, 111], [537, 699, 497, 131, 956],
#            [805, 732, 524, 37, 331]]

# at first compute a relative column sum among elements
# this array will be 3-dims and with the convention j1 < j2 for relative sum (j, i1, i2)  
relative_col_sums = np.zeros([n, n, n])
for j in range(n):
    for i_start in range(n):
        for i_end in range(i_start, n):
            relSum = 0
            for i in range(i_start, i_end+1):
                relSum += array80[i][j]
            relative_col_sums[j, i_start, i_end] = relSum

for i in range(n):
    mindist[i, 0]=array80[i][0]

for j in range(1, n):
    for i in range(n):
        for start_i in range(i+1):
            for break_i in range(start_i, i+1):
                min_dist = mindist[start_i, j-1] + relative_col_sums[j-1, start_i, break_i] + relative_col_sums[j, break_i, i]
                min_dist -= array80[start_i][j-1]
                if mindist[i, j] == 0 or min_dist < mindist[i, j]:
                    mindist[i, j] = min_dist
        for start_i in range(i+1, n):
            for break_i in range(i+1, start_i+1):
                min_dist = mindist[start_i, j-1] + relative_col_sums[j-1, break_i, start_i] + relative_col_sums[j, i, break_i]
                min_dist -= array80[start_i][j-1]
                if mindist[i, j] == 0 or min_dist < mindist[i, j]:
                    mindist[i, j] = min_dist

minPathSum = 10000000000000000
print(mindist)
for i in range(n):
    if mindist[i,n-1] < minPathSum:
        minPathSum = mindist[i,n-1]

print(minPathSum)