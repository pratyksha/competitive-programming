n = int(input())
c = [int(i) for i in input().split()]
sum_c = sum(c)
n = (-1 + (1 + 4*2*sum_c)**(1/float(2))) / 2
m = (-1 - (1 + 4*2*sum_c)**(1/float(2))) / 2
if max(m,n,0) != 0 and max(m,n,0) == max(int(m),int(n), 0):
    print("YES")
else:
    print("NO")
