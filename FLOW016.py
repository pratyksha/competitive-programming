def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m%n)
for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    res_gcd = gcd(a, b)
    res_lcm = a*b//res_gcd
    print(res_gcd, res_lcm)
