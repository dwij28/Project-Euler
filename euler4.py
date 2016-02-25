def isPalin(x): return str(x) == str(x)[::-1]
ans = 0
for i in range(101,1000):
	for j in range(101,1000):
		ans = i*j if (isPalin(i*j) and ans < i*j) else ans
print ans