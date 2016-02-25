def fact(n): return 1 if n == 0 else n*fact(n-1)
x = 0
for i in str(fact(100)): x += int(i)
print x