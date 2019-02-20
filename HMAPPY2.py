def gcd(m, n):
    if n == 0:
        return(m)
    return(gcd(n, m%n))
for _ in range(int(input())):
    n, a, b, k = [int(i) for i in input().split()]
    lcm = a*b / gcd(a,b)
    if  (n//a)+(n//b)-(2*(n//lcm)) >= k:
        print("Win")
    else:
        print("Lose")
