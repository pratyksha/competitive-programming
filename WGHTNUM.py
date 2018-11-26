for t in range(int(input())): # number of test cases
    n, w = [int(i) for i in input().split()] #  n = number of digits and w = the required weight.
    ct = 0
    for i in range(1,10):
        for j in range(10):
            if j-i == w:
                ct += 1
    print((ct*pow(10, n-2, 10**9+7))%(10**9+7)) # n digit positive integer with weight w
