for t in range(int(input())): # number of test cases
    n = int(input()) # number of elements in a
    a = [int(i) for i in input().split()]
    result = a[0]
    for i in a[1:]:
        result = result^i
    print(result<<1) # new sequence
