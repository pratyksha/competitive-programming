for _ in range(int(input())):
    n = int(input())
    chef = []
    chefa = [0]*(n+1)
    for i in range(2,4):
        print(1,i-1,i,i+1)
        chef.append(int(input()))
    curr = chef[0]^chef[1]
    chef.append(curr)
    chef_val = 0
    print(1,1,4,5)
    chefs_val = int(input())
    chefa[5] = (chefs_val^curr)
    print(1,1,4,6)
    
    chefs_val = int(input())
    chefa[6] = (chefs_val^curr)    
    i, j, k = 5, 6, 7         
    while k <= n:
         print(1,i,j,k)
         chefs_val = int(input())
         curr = chefa[i]^chefa[j]
         chefa[k] = (chefs_val^curr)
         i += 1
         j += 1
         k += 1
    curr = chefa[i]^chefa[j]    
    print(1,i,j,2)
    chefa[2] = curr^int(input())
    curr = chefa[5]^chefa[n]
    print(1,5,n,3)
    chefa[3] = curr^int(input())
    chefa[1] = chef[0]^chefa[2]^chefa[3]
    chefa[4] = chef[1]^chefa[2]^chefa[3]
    print(2,*chefa[1:])
    verdict = int(input())
        
