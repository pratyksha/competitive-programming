for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=len(set(a))
    if b == n:
        print(0)
    else:
        ct=n-b
        print(ct)
