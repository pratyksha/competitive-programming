for t in range(int(input())):
        s=input()
        cn=0
        for i in range(len(s)-1):
                if s[i]=='C':
                        if s[i+1]!='C' and s[i+1]!='E' and s[i+1]!='S':
                                cn+=1
                elif s[i]=='E':
                        if s[i+1]!='E' and s[i+1]!='S':
                                cn+=1
                elif s[i]=='S':
                        if s[i+1]!='S':
                                cn+=1
        if cn>0:
                print("no")
        else:
                print("yes") 
