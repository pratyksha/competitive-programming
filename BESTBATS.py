def factorial(x):
	fact = 1
	for i in range(2,x+1):
		fact *= i
	return fact
 
for _ in range(int(input())):
	l = list(map(int, input().split()))
	k = int(input())
	l = sorted(l, reverse = True)
	part = l[:k]
	minn = min(part)
	a = l.count(minn)
	b = part.count(minn)
	numerator = factorial(a)
	denominator = factorial(b)*factorial(a-b)
	result = numerator//denominator
	print(result)
