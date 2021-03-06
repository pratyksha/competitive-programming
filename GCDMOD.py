mod = 10**9+7
def factor(n):
    factors = []
    for i in range(1,int(pow(n, 0.5) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return list(set(factors))
for t in range(int(input())): # number of test cases   
    a, b, n = [int(i) for i in input().split()]
    if a == b:
        print((pow(a,n,mod)+pow(b,n,mod))%mod) # gcd(a^n + b^n)
        continue
    fac = sorted(factor(abs(a-b)))
    for i in fac[::-1]:
        gcd = (pow(a,n,i)+pow(b,n,i))%i
        if gcd == 0:
            print(i%mod) # gcd(|a-b|)
            break
