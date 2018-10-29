for t in range(int(input())): # number of test cases
        n=int(input()) # number of tunnels
        a=[int(i) for i in input().split()] # time to process every i-th car at the toll booth in the tunnels
        c,d,s=[int(i) for i in input().split()] # number of cars, distance between consecutive tunnels, velocity of each car
        print(float(max(a)*(c-1))) # time delay between first and last car
