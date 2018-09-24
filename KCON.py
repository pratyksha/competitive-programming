def Sum(a, size):
    max_rn=a[0]
    max_till_now=a[0]
    for i in range(1,size):
        max_rn=max( a[i],max_rn+a[i])
        max_till_now=max(max_till_now,max_rn)
    return max_till_now
for t in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    ss=sum(a)
    b=[]
    if ss==Sum(a,n):
        print(ss*k)    
    elif k==1:
        print(Sum(a,n))
    elif k==2 or k==3:
        b=a*k
        print(Sum(b,k*n))
    elif ss<=0:
        b=2*a
        if Sum(b,2*n)<=Sum(a,n):
            print(Sum(a,n))
        else:
            print(Sum(b,2*n))
    elif ss>0:
        b=2*a
        print(ss*(k-2)+Sum(b,2*n))
    else:
        b=3*a
        print((Sum(b,3*n)-Sum(b,2*n))*(k-1)+Sum(a,n)) 
