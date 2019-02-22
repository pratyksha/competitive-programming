for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = [int(i) for i in input().split()]
    stat = [a[1]+a[n-1]]
    for i in range(1,n-1):
        stat.append(a[i-1]+a[i+1])
    stat.append(a[n-2]+a[0])
    ct = 0
    maxx = -1
    for i in range(n):
        if stat[i] < d[i]:
            if maxx < d[i]:
                maxx = d[i]
    print(maxx)
