for _ in range(int(input())): # number of test cases
    chef, cook, k = [int(i) for i in input().split()] # number of points scored by Chef, Cook, value of k
    if (chef+cook) % (2*k) < k:
        print("CHEF") # Chef's turn
    else:
        print("COOK") # Cook's turn
    
