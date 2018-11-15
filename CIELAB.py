a,b = [int(i) for i in input().split()] # input
st = a-b # difference of a and b
if st % 10 == 9: # checking is the result's unit digit is 9
   #print(st)
    print(st-1) # then print (result - 1)
else:
    print(st+1) # else print (result + 1)
