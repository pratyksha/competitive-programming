for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    count = 0
    suma = sum(a)
    for i in a:
        if (i + k) > (suma - i):
            count += 1
    print(count)
