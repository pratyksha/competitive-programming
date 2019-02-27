for _ in range(int(input())):
    n = int(input())
    s = input()
    val = s.count('1')
    print(val*(val+1)//2)
