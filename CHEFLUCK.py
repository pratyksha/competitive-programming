for _ in range(int(input())):
    n = int(input())
    flag = 0
    for i in range(7):
        if (n-i*4) < 0:
            break  
        if (n-i*4) % 7 == 0:
            flag = 1 
            print(n-i*4)
            break
    if flag == 0:
        print(-1)
