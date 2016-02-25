import math
def primeFactors(n):
    factors = 0
    if (n % 2 == 0):
        factors += 1
        while (n % 2 == 0): n /= 2
    sqrtN = int(math.sqrt(n))
    for i in range(3, sqrtN + 1):
        if (n % i == 0):
            factors += 1
            while (n % i == 0): n /= i
    if n > 2: factors += 1
    return factors

f = []
#for i in range(130001, 140001): f.append(str(primeFactors(i))) --> hit and trial
#x = "".join(f)
#print x.index('4444')
print 130001+4042 # 4042 is index
print primeFactors(134041)
print primeFactors(134042)
print primeFactors(134043) # ans
print primeFactors(134044)
print primeFactors(134045)
print primeFactors(134046)