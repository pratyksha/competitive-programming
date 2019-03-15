for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    lst1 = []
    lst2 = []
    res = 0
    a = sorted(a)
    for i in range(n//2):
        lst1.append(a[i])
    for i in range(n//2,n):
        lst2.append(a[i])
    for i in range(n//2):
        res = res + (lst1[i]-lst2[i])
    print(abs(res))
