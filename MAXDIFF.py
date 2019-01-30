for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    w = sorted(w)
    son_op1 = 0
    son_op2 = 0
    for i in range(k):
        son_op1 += w[i]
        son_op2 += w[n-i-1]
    diff = sum(w) - 2*son_op1
    if diff < 0:
        diff = diff*(-1)
    diff2 = sum(w) - 2*son_op2
    if diff2 < 0:
        diff2 = diff2*(-1)
    print(max(diff,diff2))
