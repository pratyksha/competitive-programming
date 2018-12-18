def partition_it(n,sums,x):
    a = [0 for i in range(n)]
    a[x-1] = 2
    for j in range(n,0,-1):
        if a[j-1] != 2:
            if j <= sums and (sums-j) != x:
                a[j-1] = 1
                sums -= j
    return(a)
for t in range(int(input())): # number of test cases
    x,n = [int(i) for i in input().split()]
    sums = (n*(n+1)//2)-x
    if n <= 3:
        print("impossible")
    elif sums % 2 != 0:
        print("impossible")
    else:
        a = partition_it(n,sums//2,x)
        st="".join(str(e) for e in a)
        print(st)
