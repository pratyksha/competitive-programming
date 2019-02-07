def output(number):
    x = number.split('/')
    print(*x, end = " ")
from fractions import Fraction
inpt = [int(i) for i in input().split()]
for i in range(1, inpt[0]+1):
    n = inpt[i]
    val = 1/2
    ans = 1/4
    if n == 1:
        output(str(Fraction(val)))
    elif n == 2:
        output(str(Fraction(ans)))
    else:
        for j in range(n-2):
            real_ans = (ans + val) / 2
            val = ans
            ans = real_ans
        output(str(Fraction(real_ans)))
