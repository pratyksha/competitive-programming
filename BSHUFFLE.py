n = int(input())
a = [i for i in range(1,n+1)] # input array containing n integers
if n == 2:
    print(1,2) # permutation P1 : maximum possible permutation for n = 2
    print(2,1) # permutation P2 : minimum possible permutation for n = 2
elif n == 3:
    print(1,3,2) # permutation P1 : maximum possible permutation for n = 3
    print(1,2,3) # permutation P2 : minimum possible permutation for n = 3
else:
    min_a = []
    min_a.append(n)
    for i in range(1,n):
        min_a.append(i)
    max_a = []
    mid = (1+n) // 2    
    for i in range(2,mid+1):
        max_a.append(i)
    max_a.append(1)
    for i in range(mid+2,n+1):
        max_a.append(i)
    if n > 2:
        max_a.append(mid+1)

    print(*max_a) # permutation P1 : maximum possible permutation
    print(*min_a) # permutation P2 : minimum possible permutation
