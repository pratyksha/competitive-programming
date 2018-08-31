for t in range(int(input())):
    n = int(input())
    a = [[]]*n
    for i in range(n):
        a[i] = [int(k) for k in input().split()]    
    for i in range(n-1,0,-1):
        for j in range(i):
            a[i-1][j] += max(a[i][j],a[i][j+1])
    print(a[0][0])
