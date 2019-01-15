def Search(lo,hi,p,prev):
    while lo<hi:
        mid=(lo+hi)//2
        if p[mid]<prev:
            if p[mid+1]<prev:
                lo=mid+1
            else:
                return mid
        else:
            hi=mid-1
    if p[lo]>=prev:
        return -1
    return lo
for t in range(int(input())): # number of test cases 
    n=int(input())
    l=[]
    sums=0
    prev=0
    pos=0
    for i in range(n):
        l.append([int(x) for x in input().split()])
    for i in range(n-1,-1,-1):
        l[i].sort()
        if i==n-1:
            prev=l[n-1][n-1]
            sums+=prev
        else:
            pos=Search(0,n-1,l[i],prev)
            if pos==-1:
                print(-1)
                break
            prev=l[i][pos]
            sums+=prev            
    if pos!=-1:
        print(sums)
