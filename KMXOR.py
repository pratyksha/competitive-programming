for t in range(int(input())): # number of test cases
    n, k = [int(i) for i in input().split()] # n = number of ingredients, k = max-amount of ingredient
    if n == 1:
        print(k)
        continue
    elif n != 1 and k <= 3:
        if k == 3 and n%2 == 0:
            taste = [2]+[1]*(n-1)
        else:
            taste = [k]+[1]*(n-1)
    else:
        po = 2
        while po <= k:
            po = po*2
        po = po // 2
        taste = [po, po-1-n%2] + [1]*(n-2)
    print(*taste) # amounts of all ingredients to get max-taste
