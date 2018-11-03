for t in range(int(input())): # number of test cases
    s=input() # preprocessed sentence
    mins=0
    # all possible combinations of chef
    st=['chef', 'hcef', 'hecf', 'hefc', 'cehf', 'echf', 'ehcf', 'ehfc', 'cefh', 'ecfh', 'efch', 'efhc', 'chfe', 'hcfe', 'hfce', 'hfec', 'cfhe', 'fche', 'fhce', 'fhec', 'cfeh', 'fceh', 'fech', 'fehc'] 
    for word in st:
        mins+=s.count(word) 
    if mins==0:
        print("normal")
    else:
        print("lovely",end=" ")
        print(mins) # number of ways to select four contiguous characters
