for t in range(int(input())): # number of test cases 
        n=int(input())
        a=[int(i) for i in input().split()]
        p=max(a)
        print(n-p) # print the answer 
