fib=[0,1]
while fib[-1] < 4000000: fib.append(fib[-1]+fib[-2])
fib = filter(lambda x: x % 2 == 0, fib)
print sum(fib)