def farey_function(n, descending=False):
    """Print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n-1
    print ("%d/%d" % (a,b))
    mesa = False
    total=0
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        #print ("%d/%d" % (a,b))
        if a == 1 and b == 3:
            mesa = True
        if mesa == True:
            total+=1
            if a == 1 and b == 2:
                mesa = False
    return (total-2)

print(farey_function(12000))

print('73 finished')