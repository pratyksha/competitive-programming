def hash_it(arr, s): # to count occurences of each letter and returning a reverse sorted array
    for i in range(len(s)):
        arr[ord(s[i]) - 65] += 1 # counting occurences of each letter
    arr = sorted(arr, reverse = True) # reverse sorting the array
    return arr
def balance(s, arr, l): # balancing the string
    val = len(set(s))
    res = 10000000000
    pp = 0
    for p in range(1,27):
        ptr = 0
        if l % p == 0:
            var = l // p
            for q in range(p):
                if arr[q] > var:
                    ptr += arr[q] - var
            for q in range(p,26):
                if arr[q] > 0:
                    ptr += arr[q]
            res = min(ptr,res)
        pp += 1
    if pp == 26:
        pp = 0        
    return(res) 
    
for _ in range(int(input())): # number of test cases
    s = input() # input string
    l = len(s) # length of the string
    if l <= 2: # if length is 2 or less, it is already balanced
        print(0)
        continue
    arr = [0 for i in range(0,27)]
    arr = hash_it(arr,s)
    print(balance(s, arr, l))
    
    
    
    
    
    
        
