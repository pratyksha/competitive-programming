for _ in range(int(raw_input())):# Running for the given number of test cases
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]# Accepting input
    b = list(set(a))
    c = []
    ct = 0
    for i in range(len(b)):
        c.append(a[b[i]-1])#Creating the list c
    d = set(c)
    if len(c) != len(d):
        print("Truly Happy")#If necessary condition is met
    else:
        print("Poor Chef")#If condition is not met
