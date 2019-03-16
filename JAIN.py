for _ in range(int(input())):
    n = int(input())
    ingredients = [0 for i in range(32)]
    for i in range(n):
        val = set(input())
        num = 0
        for j in val:
            if j == 'a':
                num += 10000
            elif j == 'e':
                num += 1000
            elif j == 'i':
                num += 100
            elif j == 'o':
                num += 10
            elif j == 'u':
                num += 1
        value = int(str(num),base = 2)
        ingredients[value] = ingredients[value] + 1
    count = 0
    for i in range(1,31):
        for j in range(i+1,32):
            if ingredients[i] and ingredients[j] and i|j == 31:
                count += ingredients[i]*ingredients[j]
    count += (ingredients[31]*(ingredients[31]-1))//2
    print(count)
