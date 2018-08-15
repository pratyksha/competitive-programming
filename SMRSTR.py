for t in range(int(input())):
        n,q= map(int, input().split())
        d=[int(i) for i in input().split()]
        x=[int(i) for i in input().split()]
        dn=1
        for i in range(n):
                dn=dn*d[i]
        for i in range(q):
                print(x[i]//dn, end=" ")
        print() 
