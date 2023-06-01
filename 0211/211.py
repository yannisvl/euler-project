import time

# Start the timer
start_time = time.time()

# loop invariant is: after executing the loop for value i,
# arr[j] stores sigma_2(j) for 0 <= j <= i
# for all larger j, arr[j] = j's smallest prime factor if it's <= i
# otherwise, arr[j] = j
arr = list(range(64 * 10 ** 6))
sum = 1 # sigma_2(1) is a square
for i in range(2, len(arr)):
    if arr[i] != i: # composite; just compute sigma_2
        j = i
        prod = 1
        while j % arr[i] == 0:
            j /= arr[i]
            prod = arr[i]**2 * prod + 1
        arr[i] = arr[int(j)] * prod
        if int(arr[i]**.5 + .5)**2 == arr[i]:
            sum += i
    else: # prime; just sieve
        k = i * i
        while k < len(arr):
            if arr[k] == k:
                arr[k] = i
            k += i
        arr[i] = i**2 + 1


el = time.time() - start_time
print (sum)
print (el)