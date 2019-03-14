for _  in range(int(input())):
    n, d = [i for i in input().split()]
    a = [int(i) for i in n]
    d = int(d)
    n = len(a)
    i = 0
    s = ''
    while i < n:
        m = min(a[i:])
        if m < d:
            c = a[i:].count(m)
            i = len(a)-1-a[::-1].index(m)
            i = i+1 
            s = s+(str(m)*c)
        else:
            break
    print(s+(str(d)*(n-len(s))))
            
        
    
    
