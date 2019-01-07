for t in range(int(input())): # number of test cases
        s=input()
        st=[]
        count=0
        for i in range(len(s)-1):
            if s[i]+s[i+1] not in st:
                count+=1
            st.append(s[i]+s[i+1])            
        print(count) # print the answer 
