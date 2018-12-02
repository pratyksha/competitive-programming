for t in range(int(input())): # number of test cases
    arr = [int(i) for i in input().split()] # n numbers
    maxa = max(arr)
    if (len(arr) - 1) != maxa:
        print(maxa) # max value of the n numbers
    else:
        arr.remove(len(arr)-1)
        print(max(arr)) # max value of the n numbers
