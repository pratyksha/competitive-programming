a,n,k = [int(i) for i in input().split()]
ans = [0]*k
i = 0
for i in range(k):
    ans[i] = a%(n+1)
    a //= (n+1)
    if a == 0:
        break
for i in ans:
    print(i) # print the answer 
