i=1
t=""
while len(t)<=1000000:
    t = t + str(i)
    i=i+1

result = int(t[0])*int(t[9])*int(t[99])*int(t[999])*int(t[9999])*int(t[99999])*int(t[999999])
print(result)