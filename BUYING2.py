for _ in range(int(input())):
    n, x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    money_given = sum(a)
    no_of_sweets = money_given // x
    if no_of_sweets == (money_given - min(a)) // x:
        print(-1)
    else:
        print(no_of_sweets)
