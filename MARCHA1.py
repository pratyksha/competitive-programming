for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    my_notes = [0]
    for _ in range(n):
        my_notes.append(int(input()))
    s, k, ct = 0, 1, 0
    x = [0]*(20000)
    x[k] = 1
    while(1):
        if k <= n and x[k] == 1:
            if s+my_notes[k] == m:
                ct +=1
                x[k] = 0
            elif s+my_notes[k] < m:
                s+=my_notes[k]
            else:
                x[k] = 0
        else:
            k-= 1
            while k>0 and x[k] == 0:
                k-=1
            if k == 0:
                break
            x[k] = 0
            s -= my_notes[k]
        k += 1
        x[k] = 1
   
        
    if ct == 0: 
        print('No')
    else:
        print('Yes')
