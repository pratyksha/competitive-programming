for i in range(int(input())): # number of test cases
    x1, x2, x3, v1, v2 = [int(x) for x in input().split()] # position of Chef's restaurant X1, position of Kefa's restaurant X2,  position of the bottle is X3
    d1 = abs(x3 - x1)
    t1 = d1 / v1 # time = distance / speed
    d2 = abs(x3 - x2)
    t2 = d2 / v2 # time = distance / speed

    if t1 < t2:
        print("Chef") # chef reaches the bottle first 
    elif t2 < t1:
        print("Kefa") # kefa reaches the bottle first
    else:
        print("Draw") # draw
