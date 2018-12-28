from bisect import bisect_left as bl
from bisect import bisect_right as br
mylist=[]
for i in range(50):
    mylist.append(2**i) 
for t in range(int(input())): #number of test cases 
    n = int(input())
    if n == 1:
        print(2)
        continue
    if n in mylist:
        print(1)
        continue
    leftpos=bl(mylist,n)-1
    leftval=mylist[leftpos]
    leftover= n-leftval
    if leftover in mylist:
        print(0)
    else:
        pos=bl(mylist,leftover)-1
        right = mylist[leftpos+1]-n+1
        left = mylist[pos]
        posright = mylist[pos+1]
        if mylist[pos] == leftval:
            result = min(right, posright - leftover)
        elif mylist[pos+1] == leftval:
            result = min(right, leftover - left)
        else:
            result = min(posright-leftover,leftover-left,right)
        print(result)
