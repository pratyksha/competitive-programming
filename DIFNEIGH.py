for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    sol = [[0 for i in range(m)]for i in range(n)]
    count = 0
    if n == 1:
        count = 1
        for j in range(m):
            sol[0][j] = count            
            if j & 1 != 0:
                if count&1 == 0:
                    count = 1
                else:
                    count = 2
    elif m == 1:
        count = 1
        for i in range(n):
            sol[i][0] = count            
            if i & 1 != 0:
                if count&1 == 0:
                    count = 1
                else:
                    count = 2
    elif n == 2:
        for i in range(2):
            for j in range(m):                   
                if (j+1) % 3 == 2:
                    sol[i][j] = 2
                elif (j+1) % 3 == 0:
                    sol[i][j] = 3
                else:
                    sol[i][j] = 1
    elif m == 2:
        for i in range(2):
            for j in range(n):                   
                if (j+1) % 3 == 2:
                    sol[j][i] = 2
                elif (j+1) % 3 == 0:
                    sol[j][i] = 3
                else:
                    sol[j][i] = 1
    else:
        for i in range(n):
            for j in range(m):
                if count & 1 == 0:
                    if (j+1) % 4 == 0:
                        sol[i][j] = 4                    
                    elif (j+1) % 4 == 2:
                        sol[i][j] = 2
                    elif (j+1) % 4 == 3:
                        sol[i][j] = 3
                    else:
                        sol[i][j] = 1
                else:
                    if (j+1) % 4 == 0:
                        sol[i][j] = 2                    
                    elif (j+1) % 4 == 2:
                        sol[i][j] = 4
                    elif (j+1) % 4 == 3:
                        sol[i][j] = 1
                    else:
                        sol[i][j] = 3
            if i&1 != 0:
                count += 1
    print(max(max(sol)))
    for i in range(n):
        for j in range(m):
            print(sol[i][j], end = " ")
        print()
            
        
