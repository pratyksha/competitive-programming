for t in range(int(input())): # number of test cases
    n,r = [int(i) for i in input().split()] # number of people chef meets, Reziba's rating
    a = [int(i) for i in input().split()] # ratings
    prevl = max(a)
    prevr = min(a)
    for i in a:
        if i > r:
            if prevl >= i:
                prevl = i
            else:
                print("NO")
                break
        elif i < r:
            if prevr <= i:
                prevr = i
            else:
                print("NO")
                break
        else:
            print("YES")
