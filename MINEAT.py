def check(a,i):# calculating the hours taken if i bananas are eaten
    hr=0
    for j in a:
        if j%i==0: #if divisible
            hr+=(j//i)
        else:
            hr+=(j//i)+1
    return(hr)
for t in range(int(raw_input())):
    n,h=raw_input().split()
    a=[int(i) for i in raw_input().split()]
    a=sorted(a)
    lo=1 #lower bound
    hi=a[-1] #upper bound
    pos=a[-1] #final position
    while lo<=hi:
        midpt=(lo+hi)//(len("ab")) #mid point
        if check(a,midpt)>int(h): #if no. of hrs taken > given hrs
            lo=midpt+1 #shift lower bound
        elif check(a,midpt)<=int(h): #if no. of hrs taken <= given hrs
            if midpt>1 and check(a,midpt-1)<=int(h):
                hi=midpt-1 #shift upper bound
            else:
                pos=midpt
                break
    print(pos) 
