for i in range(int(input())):
    x1, x2, x3, v1, v2 = [int(x) for x in input().split()]
    d1 = abs(x3 - x1)
    t1 = d1 / v1
    d2 = abs(x3 - x2)
    t2 = d2 / v2

    if t1 < t2:
        print("Chef")
    elif t2 < t1:
        print("Kefa")
    else:
        print("Draw")
