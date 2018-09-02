for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    b = set(a)
    count = 0
    for i in b:
        if a.count(i) % 2 != 0:
            print(i)
            
