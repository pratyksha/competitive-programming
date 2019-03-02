for _ in range(int(input())):
    s, e, l, r = [i for i in input().split()]
    day_dict = { "saturday":1,"sunday":2, "monday":3, "tuesday":4, "wednesday":5, "thursday":6, "friday":7}
    l = int(l)
    r = int(r)
    durr = day_dict[e]-day_dict[s]+1
    num = 0
    time_spent = 0
    for i in range(durr, r+1,7):
        if i>=l and i<=r:
            num += 1
            time_spent = i
    if num > 1:
        print("many")
    elif num == 0:
        print("impossible")
    else:
        print(time_spent)
    
        
        
    
