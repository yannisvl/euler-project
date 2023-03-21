import numpy as np

def solve(a,c,solved, stacked):
    a11 = a[0:3, 0:3]
    a21 = a[3:6, 0:3]
    a31 = a[6:9, 0:3]
    a12 = a[0:3, 3:6]
    a22 = a[3:6, 3:6]
    a32 = a[6:9, 3:6]
    a13 = a[0:3, 6:9]
    a23 = a[3:6, 6:9]
    a33 = a[6:9, 6:9]
    total = 0
    for i in range(9):
        for j in range(9):
            if a[i,j]==0:
                total+=1
    allages = 0
    while (not solved) and (not stacked):
        allagesprin = allages
        for i in range(9):
            for j in range(9):
                if a[i,j]==0:
                    for x in a[i]:
                        if x!=0:
                            if c[i, j, int(x-1)]==1:
                                c[i, j, int(x-1)]=0
                    for x in a[:,j]:
                        if x!=0:
                            if c[i, j, int(x-1)]==1:
                                c[i, j, int(x-1)]=0
                    if i<3 :
                        if j<3:
                            b = a11
                        elif j<6:
                            b = a12
                        else :
                            b = a13
                    elif i<6:
                        if j<3:
                            b = a21
                        elif j<6:
                            b = a22
                        else :
                            b = a23
                    else:
                        if j<3:
                            b = a31
                        elif j<6:
                            b = a32
                        else :
                            b = a33
                    for row in range(3):
                        for column in range(3):
                            if b[row,column]!=0:
                                if c[i, j, int(b[row,column])-1]==1:
                                    c[i, j, int(b[row, column]) - 1]=0
                    upopshfioi = 0
                    for k in range(9):
                        if c[i, j, k] == 1:
                            upopshfioi+=1
                            bale = k
                    if upopshfioi == 1:
                        a[i, j] = bale+1
                        allages += 1
                        for kiallhgrammh in range(9):
                            if c[kiallhgrammh, j, bale]==1:
                                c[kiallhgrammh, j, bale] =0
                        for kiallhsthlh in range(9):
                            if c[i, kiallhsthlh, bale]==1:
                                c[i, kiallhsthlh, bale] =0
                        if i < 3:
                            xorio1 = 0
                            xorio2 = 3
                            if j < 3:
                                yorio1 = 0
                                yorio2 = 3
                            elif j < 6:
                                yorio1 = 3
                                yorio2 = 6
                            else:
                                yorio1 = 6
                                yorio2 = 9
                        elif i < 6:
                            xorio1 = 3
                            xorio2 = 6
                            if j < 3:
                                yorio1 = 0
                                yorio2 = 3
                            elif j < 6:
                                yorio1 = 3
                                yorio2 = 6
                            else:
                                yorio1 = 6
                                yorio2 = 9
                        else:
                            xorio1 = 6
                            xorio2 = 9
                            if j < 3:
                                yorio1 = 0
                                yorio2 = 3
                            elif j < 6:
                                yorio1 = 3
                                yorio2 = 6
                            else:
                                yorio1 = 6
                                yorio2 = 9
                            for kiallhgrammh in range(xorio1, xorio2):
                                for kiallhsthlh in range(yorio1, yorio2):
                                    if c[kiallhgrammh, kiallhsthlh, bale]==1:
                                        c[kiallhgrammh, kiallhsthlh, bale] = 0
                else:
                    for k in range(9):
                        c[i,j,k] = 0
        for grammes in range(9):
            for bathos in range(9):
                sum = 0
                thesh = -1
                for sthlh in range(9):
                    if c[grammes, sthlh, bathos] == 1:
                        sum += 1
                        thesh = sthlh
                if sum == 1:
                    a[grammes, thesh] = bathos+1
                    allages += 1
                    for kiallhgrammh in range(9):
                        if c[kiallhgrammh, thesh, bathos] == 1:
                            c[kiallhgrammh, thesh, bathos] = 0
                    for kiallhsthlh in range(9):
                        if c[grammes, kiallhsthlh, bathos] == 1:
                            c[grammes, kiallhsthlh, bathos] = 0
                    if grammes < 3:
                        xorio1 = 0
                        xorio2 = 3
                        if thesh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif thesh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                    elif grammes < 6:
                        xorio1 = 3
                        xorio2 = 6
                        if thesh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif thesh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                    else:
                        xorio1 = 6
                        xorio2 = 9
                        if thesh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif thesh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                        for kiallhgrammh in range(xorio1, xorio2):
                            for kiallhsthlh in range(yorio1, yorio2):
                                if c[kiallhgrammh, kiallhsthlh, bathos] == 1:
                                    c[kiallhgrammh, kiallhsthlh, bathos] = 0
        for sthlh in range(9):
            for bathos in range(9):
                sum = 0
                thesh = -1
                for grammes in range(9):
                    if c[grammes, sthlh, bathos] == 1:
                        sum += 1
                        thesh = grammes
                if sum == 1:
                    a[thesh, sthlh] = bathos+1
                    c[thesh, sthlh, bathos] = 0
                    allages += 1
                    for kiallhgrammh in range(9):
                        if c[kiallhgrammh, sthlh, bathos] == 1:
                            c[kiallhgrammh, sthlh, bathos] = 0
                    for kiallhsthlh in range(9):
                        if c[thesh, kiallhsthlh, bathos] == 1:
                            c[thesh, kiallhsthlh, bathos] = 0
                    if thesh < 3:
                        xorio1 = 0
                        xorio2 = 3
                        if sthlh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif sthlh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                    elif thesh < 6:
                        xorio1 = 3
                        xorio2 = 6
                        if sthlh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif sthlh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                    else:
                        xorio1 = 6
                        xorio2 = 9
                        if sthlh < 3:
                            yorio1 = 0
                            yorio2 = 3
                        elif sthlh < 6:
                            yorio1 = 3
                            yorio2 = 6
                        else:
                            yorio1 = 6
                            yorio2 = 9
                        for kiallhgrammh in range(xorio1, xorio2):
                            for kiallhsthlh in range(yorio1, yorio2):
                                if c[kiallhgrammh, kiallhsthlh, bathos] == 1:
                                    c[kiallhgrammh, kiallhsthlh, bathos] = 0
        if allages == total:
            solved = True
        elif allages == allagesprin:
            stacked = True
    return a, c, solved, stacked

f = open("./0096/p096_sudoku.txt", "r")
sum = 0
for numofsudoku in range(50):
    a = np.zeros([9, 9])
    grammes = 0
    f.readline()
    for metrhths in range(9):
        line = f.readline()
        for i in range(len(line) - 1):
            a[grammes, i] = int(line[i])
        grammes += 1
    print(a)
    c = np.ones([9, 9, 9])
    solved = False
    stacked = False
    a, c, solved, stacked = solve(a, c, solved, stacked)
    if solved:
        print(a)
        print(a[0,0], a[0,1], a[0,2])
        sum += a[0,0]*100+a[0,1]*10+a[0,2]
    elif stacked:
        i = 0
        oksw = False
        while i < 9 and not oksw:
            j = 0
            while j < 9 and not oksw:
                if a[i, j] == 0:
                    for k in range(9):
                        if c[i, j, k] == 1:
                            d = np.copy(a)
                            e = np.copy(c)
                            d[i, j] = k + 1
                            for axis1 in range(9):
                                if e[axis1, j, k] == 1:
                                    e[axis1, j, k] = 0
                            for axis2 in range(9):
                                if e[i, axis2, k] == 1:
                                    e[i, axis2, k] = 0
                            if i < 3:
                                xorio1 = 0
                                xorio2 = 3
                                if j < 3:
                                    yorio1 = 0
                                    yorio2 = 3
                                elif j < 6:
                                    yorio1 = 3
                                    yorio2 = 6
                                else:
                                    yorio1 = 6
                                    yorio2 = 9
                            elif i < 6:
                                xorio1 = 3
                                xorio2 = 6
                                if j < 3:
                                    yorio1 = 0
                                    yorio2 = 3
                                elif j < 6:
                                    yorio1 = 3
                                    yorio2 = 6
                                else:
                                    yorio1 = 6
                                    yorio2 = 9
                            else:
                                xorio1 = 6
                                xorio2 = 9
                                if j < 3:
                                    yorio1 = 0
                                    yorio2 = 3
                                elif j < 6:
                                    yorio1 = 3
                                    yorio2 = 6
                                else:
                                    yorio1 = 6
                                    yorio2 = 9
                                for axis1 in range(xorio1, xorio2):
                                    for axis2 in range(yorio1, yorio2):
                                        if e[axis1, axis2, k] == 1:
                                            e[axis1, axis2, k] = 0
                            solved = False
                            stacked = False
                            d, e, solved, stacked = solve(d, e, solved, stacked)
                            if solved == True:
                                print(d)
                                oksw = True
                                break
                j+=1
            i+=1
        sum += 100*d[0,0]+10*d[0,1] + d[0,2]
        print(d[0,0], d[0,1], d[0,2])
print(sum)