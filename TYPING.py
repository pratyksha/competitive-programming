def find_cost(a):
    cost=0
    for i in range(len(a)):
        if i==0:
            cost=cost+2
        else:
            if a[i]=='d' or a[i]=='f':
                if a[i-1]=='d' or a[i-1]=='f':
                    cost=cost+4
                else:
                    cost=cost+2
            elif a[i]=='j' or a[i]=='k':
                if a[i-1]=='j' or a[i-1]=='k':
                    cost=cost+4
                else:
                    cost=cost+2
    return cost
for _ in range(int(input())):
    strs = []
    for n in range(int(input())):
        strs.append(input())
    time=0
    l=[]
    for x in strs:
        if x  in l:
            time=time+(find_cost(x)//2)
        else:
            time=time+find_cost(x)
            l.append(x)
    print(time)
            
            
