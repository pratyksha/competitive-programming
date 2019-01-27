for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ct1, ct2 = 0, 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                ct1 += 1
            if j == i+1 and a[i] > a[j]:
                ct2 += 1
    if ct1 == ct2:
        print("YES")
    else:
        print("NO")
