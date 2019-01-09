for t in range(int(input())): # number of test cases
    n = int(input())
    s = [ int(i) for i in input().split()]
    s = sorted(s)
    res = []
    for i in range(n-1):
        res.append(abs(s[i+1] - s[i]))
    print(min(res))
