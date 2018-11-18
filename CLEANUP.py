for t in range(int(input())): # number of test cases
    n, m = [ int(i) for i in input().split() ] # number of jobs to do, number of jobs done
    jobDone = [ int(i) for i in input().split() ] # jobs done
    jobLeft = [ int(i) for i in range(1,n+1) if i not in jobDone ] # jobs to do
    for i in jobLeft[0::2]:
        print(i,end = " ") # to be done by chef
    print()
    for i in jobLeft[1::2]:
        print(i,end = " ") # to be done by chef's assistant
    print()
