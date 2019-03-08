for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    if len(arr) == n:
        count = 0
        k = 0
        i = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count+=1
            elif arr[i] == 0:
                if count == 0:
                    k = 1
                    break
                else:
                    count-=1
        if k == 1:
            print("Invalid")
        else:
            print("Valid")
