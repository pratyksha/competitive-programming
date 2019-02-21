for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        s.append(set(input()))
    count = 0
    for i in s[0]:
        ct = 1
        for j in s[1:]:
            if i in j:
                ct += 1
        if ct == n:
            count += 1
    print(count)
    
    
