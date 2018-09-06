for t in range(int(input())):
    n, m = [ int(i) for i in input().split() ]
    jobDone = [ int(i) for i in input().split() ]
    jobLeft = [ int(i) for i in range(1,n+1) if i not in jobDone ]
    for i in jobLeft[0::2]:
        print(i,end = " ")
    print()
    for i in jobLeft[1::2]:
        print(i,end = " ")
    print()
