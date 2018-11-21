for _ in range(int(input())):
    chef, cook, k = [int(i) for i in input().split()]
    if (chef+cook) % (2*k) < k:
        print("CHEF")
    else:
        print("COOK")
    
