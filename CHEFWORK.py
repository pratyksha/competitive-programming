n = int(input()) # number of workers
c = [int(i) for i in input().split()] # coins chef has to pay each worker
t = [int(i) for i in input().split()] # types of workers
c_1 = []
c_2 = []
c_3 = []
if t[c.index(min(c))] == 3:
    print(min(c))
else:
    for i in range(n):
        if t[i] == 1:
            c_1.append(c[i])
        elif t[i] == 2:
            c_2.append(c[i])
        elif t[i] == 3:
            c_3.append(c[i])
    if c_2 != [] and c_1 != []:
        print(min(c_2)+min(c_1)) # min coins that chef pays
    else:
        print(min(c_3)) # min coins that chef pays
                
