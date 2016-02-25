def collatz(n):
	count = 1
	while n != 1:
		n = n/2 if n % 2 == 0 else 3*n + 1
		count += 1
	return count

c, n = 0, 0

for i in range(1, 1000001):
	s = collatz(i)
	if s > c: c, n = s, i

print c, n
# ans = 525 837799 --> takes 26.6 seconds on this matchine