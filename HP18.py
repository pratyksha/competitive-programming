for _ in range(int(input())):
    n, bob, alice = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    bo, al, cmn = 0, 0, 0 
    for i in a:
        if i % bob == 0 and i % alice == 0:
            cmn += 1
        elif i % bob == 0:
            bo += 1
        elif i % alice == 0:
            al += 1
    if cmn > 0:
        if 1+bo > al:
            print("BOB")
        elif al >= 1+bo:
            print("ALICE")
    else:
        if bo > al:
            print("BOB")
        elif al >= bo:
            print("ALICE")
