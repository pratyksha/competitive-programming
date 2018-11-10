for t in range(int(input())): # number of test cases
        s=input() # activity log
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
                print("no") # record made by robot is not correct
        else:
                print("yes") # record made by robot is correct
