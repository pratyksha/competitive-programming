def check_in(curr, nexst):
    if curr < nexst:
        curr_root = int(math.sqrt(nexst-curr))
        while curr+curr_root <= n  and check(curr+curr_root) == 0:
            curr += curr_root
        for i in range(curr+1, curr_root+curr):
            if check(i)== 1:
                print(3,max(1,min(n,i)))
                return
        print(3,max(1,min(n,curr+curr_root)))
           
def check(given):
    print(1,max(1,min(n,given)))
    status = int(input())
    if status == 1:
        print(2)
    return(status)

import sys, math
n, c = [int(i) for i in  input().split()]
rt = int(math.sqrt(n))
curr = 0      
while curr+rt <= n and check(curr+rt) == 0:
    curr += rt
check_in (curr, curr+rt)
    
