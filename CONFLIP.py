for _ in range(int(input())):
    for _ in range(int(input())):
        i, n, q = [int(j) for j in input().split()]
        if i == q:
            print(n//2)
        else:
            print(n-n//2)
