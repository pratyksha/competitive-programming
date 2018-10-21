for t in range(int(input())):
    n, x, s = [int(i) for i in input().split()]
    arr = [0]*n
    arr[x-1] = 1    
    for j in range(s):
        a,b = [int(i) for i in input().split()]
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    print((arr.index(1))+1)

        
