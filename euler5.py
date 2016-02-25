def gcd(a, b):
	while b: a, b = b, a % b
	return a

def lcm(a, b): return (a*b) / gcd(a, b)

def lcm_multi(*args): return reduce(lcm, args)

print lcm_multi(*(range(1, 21)))