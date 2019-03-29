for i in range(int(input())):
    n = int(input())
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]

    l1 = sorted(list1)
    l2 = sorted(list2)
    
    hsh = {}
    for p in range(n):
        hsh[p+1] = False

    count = 0
    for k1 in range(n):
        for k2 in range(n):
            if l2[k2] >= l1[k1] and hsh[k2+1] != True:
                hsh[k2+1] = True
                count+=1
                break
    print(count)
