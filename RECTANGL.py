for t in range(int(input())):
    st=[int(x) for x in input().split()]
    c=0
    for i in st:
        if st.count(i)>=2 and st.count(i)!=3:
            c+=1
    if c%2==0 and c!=0 and c>2:
        print("YES")
    else:
        print("NO")
