for _ in range(int(raw_input())):
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    b = list(set(a))
    c = []
    ct = 0
    for i in range(len(b)):
        c.append(a[b[i]-1])
    d = set(c)
    if len(c) != len(d):
        print("Truly Happy")
    else:
        print("Poor Chef")
