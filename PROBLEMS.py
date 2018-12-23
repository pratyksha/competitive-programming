import bisect
p, s = [int(i) for i in input().split()]
rank = [[]for i in range(p)]
n = [0]*p
for j in range(p):
    sc = [int(i) for i in input().split()]
    ns = [int(i) for i in input().split()]
    mat = [[sc[i], ns[i]] for i in range(s)]
    mat = sorted(mat,key=lambda l:l[0])
    #print(mat)
    for i in range(s-1):
        if mat[i][1] > mat[i+1][1]:
            n[j] += 1
##print(n)
sortd_n = sorted(n)
##print(sortd_n)
for j in range(p):
    pos = bisect.bisect_left(sortd_n, n[j])
    rank[pos].append(j+1)
for ele in rank:
    for ele2 in ele:
        print(ele2) # print the answer 
    
