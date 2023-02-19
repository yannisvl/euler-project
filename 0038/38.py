import itertools


#def ispandigital(x):
#    for l in itertools.permutations('123456789'):
#        s=''
#        if s.join(l) == x:
#            return True
#    return False

def isPandigital(num):
	return len(num) == 9 and set(num) == set("123456789")

max = 0

for n in range (1, 5):
    for l in itertools.permutations('123456789', n):
        s=''
        s = s.join(l)
        print(s)
        num = ''
        for k in range (1, 9//len(s)+1):
            p = k * int(s)
            num = num + str(p)
            if isPandigital(num):
                print(s, k, num)
                if int(num) > max:
                    max = int(num)
                    maxk = k
                    maxl = s
print(max, maxk, maxl)