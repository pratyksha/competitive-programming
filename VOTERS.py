import collections
n1, n2, n3 = [int(i) for i in input().split()]
l1 = []
l2 = []
l3 = []
for i in range(n1):
    l1.append(int(input()))
for i in range(n2):
    l2.append(int(input()))
for i in range(n3):
    l3.append(int(input()))
final = [ i for i, ct in collections.Counter(l1+l2+l3).items() if ct > 1]
print(len(final))
for i in sorted(final):
    print(i)
