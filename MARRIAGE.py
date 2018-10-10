a,b = [ int(i) for i in input().split()]
if a < 0 and b > 0:
    print(abs(a)+b)
elif b < 0 and a > 0:
    print(abs(b)+a)
else:
    if a > b:
        print(abs(a-b))
    else:
        print(abs(b-a))
