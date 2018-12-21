for t in range(int(input())): # number of test cases
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    curr = 0
    count = 0
    for i in range(n):        
        if (a[i] - curr - b[i]) >= 0:
            count += 1
        curr = a[i]
    print(count) # printing output
            
