for t in range(int(raw_input())):
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    count = 0
    hassh = [0]*2001
    for i in a:
        hassh[ i + 1000 ] += 1
    for i in range(2001):
       if hassh[ i ] >= 1:
           for j in range(1, 2001):
               if i + (2 * j) < 2001 and hassh[ i + (2 * j)] >= 1:
                   if hassh[ i + j ] >= 1:
                       count += hassh[ i + 2*j ] * hassh[ i ]
       if hassh[ i ] > 1:
            count += (hassh[ i ] * ( hassh[ i ] - 1 )) // 2
    print(count) 
