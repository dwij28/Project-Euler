s = 0
m = 10**10
for i in range(1,1000):
	s = (s + (i**i)) % m
print s