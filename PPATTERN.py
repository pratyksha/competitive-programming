for _ in range(int(input())):
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    k = 1
    for i in range(1,n+1):
        for j in range(i):
            a[j][i-1-j] = str(k)
            k+=1
    for i in range(n-1,0,-1):
        for j in range(i):
            a[n-i+j][n-1-j]= str(k)
            k+=1
    for i in a:
        i = " ".join(i)
        print(i)
