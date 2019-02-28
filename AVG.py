for _ in range(int(input())):
    n, k, v = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    val = v*(n+k)
    val = val-sum(a)
    if val%k == 0 and val/k > 0:
        print(val//k)
    else:
        print(-1)
