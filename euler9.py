from math import sqrt, floor
def isPerfectSq(n): return int(sqrt(n))**2 == n
for a in range(1, 1000):
	for b in range(a+1, 1000):
		c = int(sqrt(a*a + b*b))
		if a + b + c == 1000 and isPerfectSq(a*a + b*b):
			print a, b, c
			print a*b*c
			break
	if a + b + c == 1000: break