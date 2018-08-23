for t in range(int(input())):
    st=[str(i) for i in input().split()]
    n=len(st)-1
    for i in range(n):
        s=str(st[i][:1]).upper()
        print(s,end=". ")
    s=str(st[n][:1]).upper()+str(st[n][1:]).lower()
    print(s)
