a = [0,1,2]
for i in range(3,1000000):
    a.append(i)
    a[i] = max(a[i],a[i//2]+a[i//3]+a[i//4])
def find_coin(n):
    if n < 1000000:
        return(a[n])
    else:
        p = find_coin(n//2)+find_coin(n//3)+find_coin(n//4)
        if p > n:
            return(p)
        else:
            return(n)        
try:
    while True:
        n = int(input())
        print(find_coin(n))
except:
    exit(0)
