for t in range(int(input())): # number of test cases
    n,m,x,k=[int(i) for i in input().split()] # n = patents, m = months, k = available workers, x = max no. of workers who can work
    s=input()
    e=0
    o=0
    for i in s:
        if i is 'E':
            e+=1
        elif i is 'O':
            o+=1
    if n>k or x==0:
        print('no')
    else:
        for m1 in range(1,m+1):
            if m1%2==0:
                if x<e:
                    n-=x
                    e-=x
                else:
                    n-=e
                    e=0
            else:
                if x<o:
                    n-=x
                    o-=x
                else:
                    n-=o
                    o=0
            if n<=0:
                break
        if n<=0:            
            print('yes') # it is possible to finish the patent case
        else:
            print('no') # it is not possible to finish the patent case
