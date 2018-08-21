for i in range(int(input())):
    a=input()
    b=input()
    superstring="abcdefghijklmnopqrstuvwxyz"
    supernumber="0123456789"
    count=0
    for j in superstring:
        if a.count(j)!=0 and b.count(j)!=0:
            if a.count(j)>b.count(j):
                count+=b.count(j)
            else:
                count+=a.count(j)
    for j in superstring.upper():
        if a.count(j)!=0 and b.count(j)!=0:
            if a.count(j)>b.count(j):
                count+=b.count(j)
            else:
                count+=a.count(j)
    for j in supernumber:
        if a.count(j)!=0 and b.count(j)!=0:
            if a.count(j)>b.count(j):
                count+=b.count(j)
            else:
                count+=a.count(j)
    print(count)
