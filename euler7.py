n = 2000000
data = [True]*n
primes = []

def mark_multiples(x):
	global data, n
	y = x+x
	while (y <= n):
		data[y-1] = False
		y += x

def sieve(n):
	if n < 2: return
	global data, primes
	for i in range(1, n):
		if data[i]:
			primes.append(i+1)
			mark_multiples(i+1)

sieve(n)
print primes[10000]