def euclid_gcd(m, n): # find gcd using Euclid algorithm
    if n == 0:
        return m
    return euclid_gcd(n, m%n)
for _ in range(int(input())):
    n, t, x,y,z = [int(i) for i in input().split()]
    if t == 1:
        if x != z:
            m = 2*n + 1 - z
            n = 2*n + 1
        else:
            m = z
            n = 2*n + 1
    elif t == 2:
        m = 2*n + 1 - 2*y
        n = 2*n + 1
    elif t == 3:
        if x != z:
            m = 2*n + 1 - x
            n =2*n + 1
        else:
            m = x
            n = 2*n + 1
    else:
        m = 2*n + 1 - 2*y
        n = 2*n + 1
    factor = euclid_gcd(m,n) 
    print(m//factor, n //factor) # divide by gcd in order to reduce m,n to lowest form

            
