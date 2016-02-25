def f(x):
	s = 0
	for i in str(x): s += int(i)**5
	return s == x

x, total = 531441, 0 # 531441 because (9**5)*5 =  531441 so no larger no. is possible
while x > 1:
	if f(x): total += x
	x -= 1

print total