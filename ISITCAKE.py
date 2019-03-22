for _ in range(int(input())):
    times = []
    for _ in range(10):
        times.append([int(i) for i in input().split()])
    count = 0
    for i in range(10):
        for j in times[i]:
            if j <= 30:
                count += 1
    if count >= 60:
        print("yes")
    else:
        print("no")
    
