def gcd( a, b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
for i in range(int(input())):
    a,b = [int(i) for i in input().split()]
    print(gcd(min(a,b),max(a,b)))
