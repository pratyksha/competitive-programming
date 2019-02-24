for _ in range(int(input())): # number of test cases
    n = int(input()) # number of junior chefs
    A = [int(i) for i in input().split()] # number of ingredients required 
    print(sum(A) - n + 1) # min number of jars required
