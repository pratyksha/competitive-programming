for _ in range(int(input())):
    s = input()
    r = s.count('R')
    g = s.count('G')
    if r != g and len(s) != 1:
        print("no")
    else:
        if len(s) == 1:
            print("yes")
        else:
            mismatch = 0
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    mismatch += 1
            if s[0] == s[len(s)-1]:
                mismatch += 1
            if mismatch == 0 or mismatch == 2:
                print("yes")
            else:
                print("no")
