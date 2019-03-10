for _ in range(int(input())):
    hero = 1
    villain = 1
    given_arr = []
    for n in range(int(input())):
        given_arr.append(input())
    ct = 0
    for given in given_arr:
        if given.endswith('man') or given.endswith('woman'):
            hero += 1
        else:
            villain += 1
        if hero == villain+2:
            print("superheroes")
            ct += 1
            break
        elif hero+3 == villain:
            ct += 1
            print("villains")
            break
    if ct == 0:
        print("draw")
