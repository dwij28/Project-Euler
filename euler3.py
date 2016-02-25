from math import sqrt
def largest_prime_factor(n):
	ans = 2 if n % 2 == 0 else 1
	while (n % 2 == 0): n /= 2
	s, f = int(sqrt(n)), 3
	while (f <= s):
		if (n % f == 0): ans = max(f, ans)
		while (n % f == 0): n /= f
		f += 2
	return ans if (n <= 2) else max(n, ans)

print largest_prime_factor(600851475143)