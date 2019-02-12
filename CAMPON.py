t = int(input())
for i in range(t):
    days = int(input())
    data = []
    for i in range(days):
        x, y = [int(x) for x in input().split()]
        data.append([x, y])

    data.sort()

    d = [0 for i in range(32)]

    for i in data:
        day = i[0]

        d[day] += i[1]

    for i in range(len(d) -1):
        d[i + 1] += d[i]

    nq = int(input())
    for i in range(nq):
        dead, req = [int(x) for x in input().split()]
        if d[dead] >= req:
            print("Go Camp")
        else:
            print("Go Sleep")
