for _ in range(int(input())):
    n = int(input())
    ans = 9999999999
    x = 1
    while x**2 <= n:
        if n % x == 0:
            y = n//x
            ans = min(ans, y-x)
        x += 1
    print(ans)
