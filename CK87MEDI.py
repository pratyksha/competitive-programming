for i in range(int(input())):
    n,k=input().split()
    b=[]
    a = [int(j) for j in input().split()]
    b=sorted(a)
    if (int(k)+int(n))//2>int(n):
        print(1000)
    else:
        print(b[((int(k)+int(n))//2)]) 
