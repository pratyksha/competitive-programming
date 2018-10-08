def calculate(st):
    a_count = 0
    b_count = 0
    count = 0
    for i in st:
##        print(i)
        if i == 'a':
            a_count += 1
        if i == 'b':
            b_count += 1
        if a_count > b_count:
            count += 1
    return(count)
for T in range(int(raw_input())):
    s, n = raw_input().split()
    n = int(n)
    a_in_s = s.count('a')
    b_in_s = s.count('b')
    if n <= 1000:
##        print(n*s)
        print(calculate(n*s))
    else:
        if a_in_s == b_in_s:
            count_2 = calculate(2*s)
            count_3 = calculate(3*s)
            print(count_2 + (count_3-count_2) * (n-2))
        if b_in_s > a_in_s:
            print(calculate(s*((b_in_s)-1)))
        if a_in_s > b_in_s:
            if set(s) == 'ab':
                print(calculate(s*(a_in_s))*n//a_in_s)
            else:
                if n < 1002:
                    print(calculate(s*(min(1002,n))))
                else:
                    print(calculate(s*(min(1002,n)))+len(s)*(n-1002))
