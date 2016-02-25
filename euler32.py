def isPandigital(n): return sorted(list(str(n))) == list("123456789")

data = []
a, b = 1, 1
# range obtained by hit and trial
for a in range(1000):
	for b in range(2000):
		x = a*b
		if isPandigital(str(a) + str(b) + str(x)): data.append(x)
print sum(set(data))