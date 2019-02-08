n, min_rating = [int(i) for i in input().split()]
rating = []
for i in range(n):
    rating.append(int(input()))
for r in rating:
    if r < min_rating:
        print("Bad boi")
    else:
        print("Good boi")
