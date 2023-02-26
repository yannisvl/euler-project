import time
start = time.time()
total = 0
for i in range(1, 10001):
    word = str(i)
    lychrel = True
    for j in range(0, 50):
        a = int(word) + int(word[::-1])
        word = str(a)
        if word==word[::-1]:
            lychrel = False
            break
    if lychrel==True:
        total += 1
print(total)
end = time.time()
print(end - start, 'sec')