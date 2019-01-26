def check_prime(val):
    if val == 1:
        return False
    if val == 2 or val == 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False 
    curr = 5
    for curr in range (5, int(val**(1/2))+1, 6):
        if val % curr == 0 or val % (curr+2) == 0:
            return False
    return True

for t in range(int(input())):
    m, n = [int(i) for i in input().split()]
    for i in range(m, n+1):
        if check_prime(i):
            print(i)
    
            
    
            
