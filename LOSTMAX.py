for t in range(int(input())):
    arr = [int(i) for i in input().split()]
    maxa = max(arr)
    if (len(arr) - 1) != maxa:
        print(maxa)
    else:
        arr.remove(len(arr)-1)
        print(max(arr))
