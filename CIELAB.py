a,b = [int(i) for i in input().split()]
st = a-b
if st % 10 == 9:
   #print(st)
    print(st-1)
else:
    print(st+1)
