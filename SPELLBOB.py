for t in range(int(raw_input())):
    card_face = raw_input()
    card_back = raw_input()
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
        
