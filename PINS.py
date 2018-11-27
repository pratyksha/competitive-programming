for t in range(int(input())):
    n = int(input())
    print(1, end = " ")
    if n%2 != 0:
        print(1,end = "")
        l = [0]*(n//2)
        print(*l, sep = "")
    else:
        print(1,end = "")
        l = [0]*((n-(n//2)))
        print(*l, sep = "")
              

