for t in range(int(input())):
    n, w = [int(i) for i in input().split()]
    ct = 0
    for i in range(1,10):
        for j in range(10):
            if j-i == w:
                ct += 1
    print((ct*pow(10, n-2, 10**9+7))%(10**9+7))
