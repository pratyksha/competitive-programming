def FinalPrice(p,q,d):
    p1=p+(p*d/100)
    p2=p1-(p1*d/100)
    p=p-p2
    return(q*p)
for t in range(int(input())): # number of testcases
    n=int(input()) # number of recipe types
    sums=0
    for i in range(n):
        p,q,d=input().split() # price, quantity, discount
        sums+=FinalPrice(int(p),int(q),int(d))
    print(sums) # total amount of money lost
