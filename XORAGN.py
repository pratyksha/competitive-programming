for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    result = a[0]
    for i in a[1:]:
        result = result^i
    print(result<<1)
