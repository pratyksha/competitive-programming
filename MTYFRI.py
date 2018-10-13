for t in range(int(raw_input())):
    n, k = [ int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    motu = a[::2]
    tomu = a[1::2]
    sum_tomu = sum(tomu)
    sum_motu = sum(motu)
    if sum_tomu > sum_motu:
        print("YES")
    elif sum_tomu <= sum_motu and k == 0:
        print("NO")
    else:           
        max_motu = max(motu)
        min_tomu = min(tomu)
        flag = 0
        while flag == 0 and k>0:
            if sum(tomu) > sum(motu):
                flag = 1
            else:
                tomu.append(max(motu))
                motu.append(min(tomu))
                tomu.remove(min(tomu))
                motu.remove(max(motu))
                k -= 1
                if sum(tomu) > sum(motu):
                    flag = 1
        if flag == 1:
            print("YES")
        else:
            print("NO")
