for t in range(int(input())): # number of testcases
    n, m, x, y = [int(i) for i in input().split()] # knowledge, power, increase in knowledge, increase in power
    if ((n-1) % x) == 0  and ((m-1) % y ) == 0 and n-1 >= 0 and m-1 >= 0:
        print('Chefirnemo') # it is possible to reach the required knowledge and power
    elif ((n-2) % x) == 0 and ((m-2) % y) == 0 and n-2 >= 0 and m-2 >= 0:
        print('Chefirnemo') # it is possible to reach the required knowledge and power
    else:
        print('Pofik') # it is not possible to reach the required knowledge and power
