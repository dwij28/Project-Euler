s = 1 # total sum
adder = 2 # the gap between two adjacent vertices that fall on the diagonal
x = 1 # will store next starting point
for i in range(500):
	for j in range(4):
		x += adder
		s += x
	adder += 2
print s