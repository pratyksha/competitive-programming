for _ in range(int(input())): # number of test cases
    n = int(input())
    a = [int(i) for i in input().split()]
    k = int(input())
    b = sorted(a)
    print((b.index(a[k-1])) + 1)
    
