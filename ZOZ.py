for t in range(int(input())): # number of test cases
    n, k = [int(i) for i in input().split()] # input value of n,k
    a = [int(i) for i in input().split()] # array elements
    count = 0
    suma = sum(a)
    for i in a:
        if (i + k) > (suma - i):
            count += 1
    print(count) # number of valid positions
