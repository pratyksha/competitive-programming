for _ in range(int(input())):
    j = input()
    s = input()
    ct = 0
    for i in s:
        if i in j:
            ct += 1
    print(ct)
