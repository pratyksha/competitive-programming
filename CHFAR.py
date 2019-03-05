for _ in range(int(input())):
    n, k = [ int(i) for i in input().split()]
    a = [ int(i) for i in input().split()]
    count_1 = a.count(1)
    if (n - count_1) <= k:
        print("YES")
    else:
        print("NO")
