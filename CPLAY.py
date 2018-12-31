try:
    while True: # to make sure code runs as long as it receives input
        inp=input()
        if inp!="":
            a=[]
            b=[]
            a1=0
            b1=0
            c=0
            for i in range(20):
                if i%2==0:
                    a.append(inp[i])
                else:
                    b.append(inp[i])
            for i in range(5):
                if a[i]=='1':
                    a1+=1
                if a1>b1+5-i:
                    print("TEAM-A ",((i+1)*2)-1)
                    c=1
                    break
                if b1>a1+4-i:
                    print("TEAM-B ",((i+1)*2)-1)
                    c=1
                    break      
                if b[i]=='1':
                    b1+=1
                if a1>b1+4-i:
                    print("TEAM-A ",(i+1)*2)
                    c=1
                    break
                if b1>a1+4-i:
                    print("TEAM-B ",(i+1)*2)
                    c=1
                    break            
            if c==0:
                for i in range(5,10):
                    if a[i]=='1':
                        a1+=1               
                    if b[i]=='1':
                        b1+=1
                    if a1>b1:
                        print("TEAM-A ",(i+1)*2)
                        c=1
                        break
                    if b1>a1:
                        print("TEAM-B ",(i+1)*2)
                        c=1
                        break
                if c==0:
                    print("TIE")
        else:
            break
except EOFError:
	pass
