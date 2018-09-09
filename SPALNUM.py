for _ in range(int(input())):
    l, r = [int(i) for i in input().split()]
    sums = 0
    for i in range(l, r+1):        
        rev = int(str(i)[::-1])
        if rev == i:
            sums += i
    print(sums)
