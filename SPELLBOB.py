for t in range(int(raw_input())): # number of test cases
    card_face = raw_input() #  characters on top faces of the first, second and third card
    card_back = raw_input() #  characters on bottom faces of the first, second and third card
    if card_face[0] == 'b' or card_back[0] == 'b':
        if card_face[1] == 'o' or card_back[1] == 'o':
            if card_face[2] == 'b' or card_back[2] == 'b':
                print("yes")
                continue
    if card_face[0] == 'o' or card_back[0] == 'o':
        if card_face[1] == 'b' or card_back[1] == 'b':
            if card_face[2] == 'b' or card_back[2] == 'b':
                print("yes")
                continue
    if card_face[0] == 'b' or card_back[0] == 'b':
        if card_face[1] == 'b' or card_back[1] == 'b':
            if card_face[2] == 'o' or card_back[2] == 'o':
                print("yes")
                continue
    print("no")
        
