for t in range(int(input())): # number of test cases
    n, d = [int(i) for i in input().split()] # number of elements in array and the size of mover
    a = [int(i) for i in input().split()] # input array 
    if sum(a)%n != 0:
        print(-1)
    else:
        p = sum(a[:])//n
        ct=0
        for i in range(n-d):
            if a[i] < p:
                a[i+d] -= (p - a[i])                
                ct += (p - a[i])
                a[i] = p
            elif a[i] > p:
                a[i+d] += (a[i] - p)                
                ct += (a[i] - p)
                a[i] = p
        if max(a) == min(a):
            print(ct) # minimum number of uses
        else:
            print(-1) # its impossible to do what Snuffles wants
