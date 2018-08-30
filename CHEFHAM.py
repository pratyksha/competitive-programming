def swap(b,i,x,n):
    if a[i] != b[i+x]:
        temp = b[i]
        b[i] = b[i+x]
        b[i+x] = temp
    elif x < n-2:
        x += 1
        swap(b,i,x,n)
    return b
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = a[::-1]
    ct = 0
    if n > 2:
        for i in range(n-1):
            x = 0
            if a[i] == b[i+x]:
                if x < n-2:
                    x +=1
                    swap(b,i,x,n)
                else:
                    break
        if a[n-1] == b[n-1]:
            if a[n-1] != b[0]:
               temp = b[n-1]
               b[n-1] = b[0]
               b[0] = temp
            elif a[n-1] != b[n//2]:
               temp = b[n//2]
               b[n//2] = b[n-1]
               b[n-1] = temp
        if a[0] == b[0]:
            if a[n-1] != b[1]:
               temp = b[0]
               b[0] = b[1]
               b[0] = temp
            elif a[0] != b[n//2]:
               temp = b[n//2]
               b[n//2] = b[0]
               b[0] = temp
    if n >= 4:
        ct = n
    else:
        for i in range(n):
            if a[i] != b[i]:
                ct += 1    
    print(ct)
    print(" ".join(str(x) for x in b))  
