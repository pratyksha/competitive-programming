for _ in range(int(input())):
    n = int(input())
    arrival = [int(i) for i in input().split()]
    departure = [int(i) for i in input().split()]
    l = [0]*1007
    for i in range(n):
        a = arrival[i]
        d = departure[i]
        for j in range(a,d):
            l[j] += 1
    print(max(l))
