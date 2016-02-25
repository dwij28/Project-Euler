from math import sqrt

def is_perfect_sq(n):
	return int(sqrt(n))**2 == n

data = [0]*1100
for i in range(1, 500):
	for j in range(i, 500):
		if is_perfect_sq(i*i + j*j):
			x = i+j+int(sqrt(i*i+j*j))
			if x <= 1000: data[x] += 1
print data.index(max(data))