for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    odd = 0
    if len(a) == 1:
        print(1)
    else:
        for ele in a:
            if ele % 2 != 0:
                odd += 1
        if odd % 2 == 0:
            print(1)
        else:
            print(2)
        
