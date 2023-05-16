p = [1, 1, 2]

# the idea is the Bell numbers which are saved in p
counter = 3
while 1:
    a = 0

    #wonderful partition identity was discovered by Euler
    for k in range(1, counter+1):
        m1 =0
        m2 =0
        t1 = int(k*(3*k - 1)/2)
        t2 = int(k*(3*k+1)/2)
        if k%2==0:
            proshmo = -1
        else :
            proshmo = +1
            
        if counter>=t1:
            a += proshmo * p[counter - t1]
            m1 = 1
        if counter>=t2:
            a += proshmo * p[counter - t2]
            m2 = 1
        if m1 + m2 == 0:
            break

    # a = bellNumber(counter)

    p.append(a)
    print(counter)
    if a%1000000==0:
        print(counter)
        break
    counter+=1
