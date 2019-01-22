for _ in range(int(input())):
    n, c = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    if c >= sum(a):
        print("Yes")
    else:
        print("No")
