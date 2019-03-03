for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)
    ct = 0
    if n==1:
        if s[0]=='0':
            print(1)
        else:
            print(0)
    else:
        if s[0] == '0' and s[1] == '0':
            s[0] = '1'
            ct += 1
        if s[-1] == '0' and s[-2] == '0':
            s[-1] = '1'
            ct += 1
        for i in range(1,n-1):
            if s[i-1]=='0' and s[i]=='0' and s[i+1]=='0':
                s[i]='1'
                ct += 1
        print(ct) 
    
        
