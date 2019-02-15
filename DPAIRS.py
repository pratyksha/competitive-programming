n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
min_b = min(b)
max_a = max(a)
a_idx = a.index(max_a)
b_idx = b.index(min_b)
for i in range(0,n):
    print(i,b_idx)
for i in range(0,m):
    if i != b_idx:
        print(a_idx, i)

