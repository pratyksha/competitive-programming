for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    count = 0
    s = sorted(s,reverse=True)
    for i in s:
        if i >= s[k-1]:
            count += 1
    print (count)
    
