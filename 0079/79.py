from itertools import permutations

def insidecode(three, code):
    i = 0
    j = 0
    while j<len(code):
        if three[i]==code[j]:
            i+=1
            if i==2:
                return True
        j+=1
    return False

f = open('./0079/p079_keylog.txt', 'r')
threes = []
for line in f:
    threes.append(list(line)[:-1])
f.close()

#the code must contain only different digits
for xx in permutations('01236789', 8):
    found = True
    for three in threes:
        if not insidecode(three, xx):
            found = False
            break
    if found and xx[0] != '0':
        print(xx)
        break
