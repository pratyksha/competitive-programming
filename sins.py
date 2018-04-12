def hcf(m,b):    
    if (m == 0):
        return b
    return hcf(b % m, m)
for t in range(int(input())):
    x, y = [ int(i) for i in input().split()]
    if x == 0:
        print(y)
    elif y == 0:
        print(x)
    else:
        print(2*hcf(x, y))
