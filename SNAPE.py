import math
for _ in range(int(input())):
    b, ls = [int(i) for i in input().split()]
    rs_min = math.sqrt(ls**2 - b**2)
    rs_max = math.sqrt(ls**2 + b**2)
    print("%f %f" %(rs_min, rs_max))
