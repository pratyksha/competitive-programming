for t in range(int(input())):  # number of test cases
    n = int(input()) # number of apple trees in Chef's garden
    apple_per_tree = [int(i) for i in input().split()] # number of apples on each tree
    sett = set(apple_per_tree) # for trees with same number of apples, all apples are plucked in a single minute
    time = 0
    for i in sett:
        time += 1
    print(time) # minimum time to pluck all apples
