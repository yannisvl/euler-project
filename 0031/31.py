coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
def ways (t, c):
    if t == 0:
        return 1
    if coins[c] == 1:
        return 1
    else :
        if t<coins[c]:
            return ways(t, c-1)
        else :
            return ways(t-coins[c], c) + ways(t, c-1)
print(ways(amount, 7))
