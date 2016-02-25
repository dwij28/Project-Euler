from math import sqrt

def count_factors(n):
	s, c = int(sqrt(n)), 0
	for i in range(1, s):
		if n % i == 0: c += 2 # numbers have 2 factors i, n/i till sqrt(n) and then if it is a perfect sq than 1 for it
	if s*s == n: c += 1 # perfect sq
	return c

i, n = 1, 1
while (n < 100000000):
	if count_factors(n) >= 500:
		print n
		break
	i += 1
	n = i*(i+1)/2