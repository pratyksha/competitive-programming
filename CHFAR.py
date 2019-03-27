for _ in range(int(input())): # number of test cases
    n, k = [ int(i) for i in input().split()]
    a = [ int(i) for i in input().split()]
    count_1 = a.count(1)
    if (n - count_1) <= k:
        print("YES") # it is possible to satisfy given condition
    else:
        print("NO") # it is not possible to satisfy given codition
