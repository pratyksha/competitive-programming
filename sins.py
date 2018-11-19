def hcf(m,b):    
    if (m == 0):
        return b
    return hcf(b % m, m)
for t in range(int(input())): # number of test cases
    x, y = [ int(i) for i in input().split()]  # x = Meliodas's chocolates and y = Ban's chocolates
    if x == 0:
        print(y)
    elif y == 0:
        print(x)
    else:
        print(2*hcf(x, y)) # number of chocolates left after fight
