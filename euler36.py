def isPalin(n): return str(n) == str(n)[::-1]

print sum([i if isPalin(i) and isPalin(bin(i)[2:]) else 0 for i in range(1, 1000000)])

# 0 does not contribute to sum hence adding 0 does not matter