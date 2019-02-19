def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
def Primes(val):
    count = 0
    i = 2
    while count < val:
        if check_prime(i):
            prime_arr.append(i)
            count += 1
        i += 1

prime_arr = []
Primes(25005)
for _ in range(int(input())):
    n = int(input())
    count = 0
    double_count = 4
    counter = 0
    if n != 3:
        while counter < n-2:
            if count % 4 == 0:
                print(2*prime_arr[double_count], end = " ")
                counter += 1
            elif count % 4 == 1:
                print(2*prime_arr[double_count+1], end = " ")
                counter += 1
            elif count % 4 == 2:
                print(3*prime_arr[double_count], end = " ")
                counter += 1
            elif count % 4 == 3:
                print(3*prime_arr[double_count+1], end = " ")
                counter += 1
            if counter % 2 == 0:
                double_count += 1
            count = (count + 1) % 4
        if n % 2 != 0:
            if count > 1:
                print(5*3, end = " ")
            else:
                print(5*2, end = " ")
        else:
            print(5*prime_arr[double_count], end = " ")
        print(11*5)
    else:
        print(2*3, 2*5, 5*3)
    
            
                
