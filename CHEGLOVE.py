for t in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    g=[int(i) for i in input().split()]
    f=0
    b=0
    for i in range(n):
        if l[i]<=g[i]:
            f+=1
    g=g[::-1]
    for i in range(n):
        if l[i]<=g[i]:
            b+=1
    if f==b==n:
        print('both')
    elif f==n:
        print('front')
    elif b==n:
        print('back')
    else:
        print('none')
