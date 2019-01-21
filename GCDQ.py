def gcd(a,b):
    if b == 0:
        return(a)
    return gcd(b,a%b)
for _ in range(int(input())):
    n, q = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    pref, suff = [0]*(n+1),[0]*(n+1)
    for i in range(1,n+1):
        pref[i] = gcd(pref[i-1],a[i-1])
    for i in range(n-1,-1,-1):
        suff[i]=gcd(suff[i+1],a[i])
    for _ in range(q):
        l, r = [int(i) for i in input().split()]
        print(gcd(pref[l-1],suff[r]))
            
