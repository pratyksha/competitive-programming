n = int(input()) # number of elements
a = [int(i) for i in input().split()] # elements of array
b = []
c = []
for i in a:
    if i != 0:
      b.append(i)
    else:
      c.append(len(b))
      b = []
c.append(len(b))
if c != []:
    print(max(c))  # max length of subarray with non-zero product
else:
    print(0)

