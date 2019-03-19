import bisect as bi
for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    l = []
    r = []
    for i in range(n):
        x,y = [int(i) for i in input().split()]
        l.append((x,i))
        r.append(y)
    l.sort(key = lambda x:x[0])
    r = [r[i[1]] for i in l]
    l = [i[0] for i in l]
    for _ in range(m):
        val = int(input())
        val2 = bi.bisect_right(l,val)
        if val2 == len(l) and val2 >= r[-1]:
            print(-1)
            continue
        if val < l[0]:
            print(l[0] - val)
            continue
        try :
            if val < r[val2 - 1]:
                print(0)
            else:
                print(l[val2] - val)
        except:
            print(-1)
