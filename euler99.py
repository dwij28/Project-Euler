from math import log
values = []
data = open("base_exp.txt", "r")
for i in data:
	a, b = map(int, i.rstrip().split(','))
	values.append(b*log(a))
print values.index(max(values)) + 1 # line number starts from 1
data.close()