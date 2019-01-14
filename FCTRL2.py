t = int(input()) #number of test cases
while t>0:
    num = int(input())
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    print(fact)
    t=t-1 
