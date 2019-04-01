for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    ind = a.index(min(a))
    count = a[ind]
    if ind == 0:
        if count == min(a[1:]):
            ind = a[1:].index(min(a[1:])) + 1
            opt = str(ind)
        else:
            opt = str(10)
    else:
        opt = str(ind)
    for i in range(count):
        opt = opt + str(ind)
    print(opt)
