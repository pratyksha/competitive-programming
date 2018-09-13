for t in range(int(input())):
    n = int(input())
    apple_per_tree = [int(i) for i in input().split()]
    sett = set(apple_per_tree)
    time = 0
    for i in sett:
        time += 1
    print(time)
