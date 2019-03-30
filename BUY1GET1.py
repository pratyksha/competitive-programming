for _ in range(int(input())):
    s = input()
    s = list(s.strip())
    cost = 0
    for i in set(s):
        ct = s.count(i)
        if ct%2 == 0:
            cost += (ct//2)
        else:
            cost += ((ct+1)//2)
    print(cost)
