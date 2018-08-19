for t in range(int(input())):
        n=int(input())
        a=[int(i) for i in input().split()]
        sa=sorted(a)
        b=[]
        c=[]
        for i in range(n,2*n):
                b.append(sa[i])
        for i in range(0,n):
                c.append(sa[i])
        print(b[(n)//2])
        for i in range(0,n):
              print(c[i],b[i],end=" ")
        print() 
