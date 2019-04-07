def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for j in range(3, int(n**0.5)+1, 2):
        if n % j == 0:
            return False
    return True


n = int(input())
if n == 1 or n == 2:
    print('2')
else:
    if n % 2 == 0:
        i = n+1
        while 1:
            if str(i) == str(i)[::-1] and isPrime(i):
                print(i)
                break
            i += 2
    else:
        i = n
        while 1:
            if str(i) == str(i)[::-1] and isPrime(i):
                print(i)
                break
            i += 2
