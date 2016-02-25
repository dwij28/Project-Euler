n = 2000000
data = [True]*n

def mark_multiples(x):
	global data, n
	y = x+x
	while (y <= n):
		data[y-1] = False
		y += x

def sieve(n):
	prime_sum = 0
	if n < 2: return prime_sum
	global data
	for i in range(1, n):
		if data[i]:
			prime_sum += (i+1)
			mark_multiples(i+1)
	return prime_sum

print sieve(n)