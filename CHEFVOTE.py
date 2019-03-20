for _ in range(int(input())):
    n = int(input())
    c = [int(i) for i in input().split()]
    if n == 1:
        print(-1)
        continue
    if sum(c) != n or n in c:
        print(-1)
        continue
    res = []
    for p in range(n):
        for q in range(c[p]):
            res.append(p+1)
    for p in range(len(res)):
        if res[p] == p+1:
            for q in range(len(res)):
                if res[q] != p+1:
                    res[p], res[q] = res[q], res[p]
                    break
    print(*res)
