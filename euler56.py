def sum_of_digits(n): return sum([int(i) for i in list(str(n))])

ans, max_sum = [], 0
for a in range(1, 101):
	for b in range(1, 101):
		x = sum_of_digits(a**b)
		if x > max_sum:
			max_sum = x
			ans = [a, b]
print ans, max_sum