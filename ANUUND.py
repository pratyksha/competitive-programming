for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort(reverse = True)
    a = arr.copy()
    for i in range(0,len(arr), 2):
        arr[i] = a.pop()
    for i in range(1,len(arr),2):
        arr[i] = a.pop()
    for i in arr:
        print(i,end = " ")
    print()
