for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    c=[]
    d=[]
    b={1,2,3,4,5,6,7}
    check=0
    if n%2==0:
        c=a[:n//2]
        d=a[(n//2):]
    else:
        c=a[:n//2]
        d=a[(n//2)+1:]
    if c!=d[::-1]:
        check=1
    if set(a)!=b:
        check=1
    if check==0:
        print("yes")
    else:
        print("no")
