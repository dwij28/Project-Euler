# pandigital number has all numbers as 1,2,3,4,5,6,7,8,9 as digits in some order
data = []
for i in range(1,100000):
	s,m = "",1
	while (len(s)<9):
		s += str(i*m)
		m += 1
	if len(s) == 9 and sorted(list(s)) == ["1","2","3","4","5","6","7","8","9"]: data.append(s)

print max(data)