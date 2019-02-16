for _ in range(int(input())):
    n, p = [int(i) for i in input().split()]
    val = n % (n//2+1)
    if val == 0:
        print(p**3)
    else:
        print(((p-val)**2)+((p-n)*(p-val))+((p-n)**2))
