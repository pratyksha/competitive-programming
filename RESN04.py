for _ in range(int(input())):
    n = int(input())
    stone = [int(i) for i in input().split()]
    ct = 0
    for i in range(n):
        ct += stone[i]//(i+1)
    if ct%2 == 0:
        print('BOB')
    else:
        print('ALICE')
