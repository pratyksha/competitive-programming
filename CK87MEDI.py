for i in range(int(input())): # number of test cases
    n,k=input().split() # array length and numbers of elements to be inserted
    b=[]
    a = [int(j) for j in input().split()] # array elements
    b=sorted(a)
    if (int(k)+int(n))//2>int(n):
        print(1000)
    else:
        print(b[((int(k)+int(n))//2)]) # greatest median after inserting k elements
