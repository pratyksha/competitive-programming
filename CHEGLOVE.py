for t in range(int(input())): # number of test cases
    n=int(input()) # number of fingers
    l=[int(i) for i in input().split()] # lengths of fingers
    g=[int(i) for i in input().split()] # lengths of sheaths of the glove
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
