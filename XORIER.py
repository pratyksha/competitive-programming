def split_it(a,n,hshh): #splits the original list - a into even and odd
    even = []
    odd = []
    for i in range(n):
        hshh[a[i]] = hshh[a[i]] + 1 
        if a[i]%2 == 0:# condition to check even >> even numbers are completely divisible by 2
            even.append(a[i])
        else: # condition for odd since a[i] is not even
            odd.append(a[i])
    return(hshh, even, odd)

def remove(hashh,len_even, len_odd, even, odd): #calculates the duplicates, even pairs and odd pairs

    dup, count_even, count_odd = 0, 0, 0    
    for i in hashh:
        dup += (i*(i-1))//2 # dup = taking xor a number with itself >> they have to be removed 

    for i in range(max(len_even-1,len_odd-1)): #even and odd pairs whose xor results in 2 >> 2 can't be written as sum of primes.
        if i < len_even-1 and (even[i+1] - even[i] == 2 and even[i] % 4 == 0):
            count_even += hashh[even[i]]*hashh[even[i+1]]
            
        if i < len_odd-1 and (odd[i+1] - odd[i] == 2 and odd[i] % 4 == 1):
            count_odd += hashh[odd[i]]*hashh[odd[i+1]]
    return(dup, count_even, count_odd)
            
for _ in range(int(input())):
    n = int(input()) # value of N is accepted
    a = [int(i) for i in input().split()] # sequence of integers A1....An is accepted
    hashh = [0]*1000001
    
    hashh, even, odd = split_it(a, n, hashh) # goes to split_it function and gets even and odd elements' list
    
    len_even = len(even)
    len_odd = len(odd)
    
    even = sorted(even)
    odd = sorted(odd)
    
    dup, count_even, count_odd = remove(hashh,len_even, len_odd, even, odd) # goes to remove function and gets the value that has to be reduced

    total_even = (len_even *(len_even-1)) // 2 # gets the total number of even pairs using n(n-1)/2 
    total_odd = (len_odd *(len_odd-1)) // 2 # gets the total number of odd pairs using n(n-1)/2 
    
    print(total_even + total_odd - (dup + count_even + count_odd))
