for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    pos = 0
    neg = 0
    for i in a:
        if i < 0:
            neg += 1
        else:
            pos += 1
    if neg > 0:
        print(max(neg, pos), min(neg,pos))
    else:
        print(pos,pos)
