for t in range(int(input())):
    m, n = [ int(i) for i in input().split()]
    a = [ int(i) for i in input().split()]
    b = [ int(i) for i in input().split()]
    res = []
    if n == 1:
        print((m*sum(a)) % 1000000007)
    elif n == 2:
        print((m*sum(b)) % 1000000007)
    else:
        res.append(m*sum(a))
        res.append(m*sum(b))
        for i in range(1,n):
            res.append(res[i-1]+res[i])
        print(res[n-1] % 1000000007) 
