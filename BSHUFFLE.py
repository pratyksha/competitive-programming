n = int(input())
a = [i for i in range(1,n+1)]
if n == 2:
    print(1,2)
    print(2,1)
elif n == 3:
    print(1,3,2)
    print(1,2,3)
else:
    min_a = []
    min_a.append(n)
    for i in range(1,n):
        min_a.append(i)
    max_a = []
    mid = (1+n) // 2    
    for i in range(2,mid+1):
        max_a.append(i)
    max_a.append(1)
    for i in range(mid+2,n+1):
        max_a.append(i)
    if n > 2:
        max_a.append(mid+1)

    print(*max_a)
    print(*min_a)
