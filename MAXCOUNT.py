for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    size = max(set(a))
    hsh = [0]*(size)
    for i in a:
        hsh[i-1] += 1
    maxc = hsh[0]
    pos = 1
    for i in range(size):
        if maxc < hsh[i]:
            maxc = hsh[i]
            pos = i+1
    print(pos,maxc)
