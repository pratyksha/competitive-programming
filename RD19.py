from functools import reduce
def hcf(num1, num2):
    if num1 == 0:
        return num2
    return hcf(num2%num1, num1)
for t in range(int(input())): # number of test cases 
    n = int(input()) # size of array a
    a = [int(i) for i in input().split()]
    hcf_all = reduce(hcf, a)
    if hcf_all != 1:
        print (-1)
    else:
        print (0)
