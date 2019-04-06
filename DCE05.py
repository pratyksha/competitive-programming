for _ in range(int(input())):
    n = int(input())
    num = 1
    while(n>=2):
        num = num*2
        n = n//2
    print(num)
