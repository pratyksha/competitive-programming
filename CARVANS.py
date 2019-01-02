for _ in range(int(input())): # number of test cases
    n = int(input())
    speeds = [int(i) for i in input().split()]
    temp = speeds[0]
    count = 1
    for i in range(1,n):
        if speeds[i]<=temp:
            temp = speeds[i]
            count += 1
    print(count)
    
