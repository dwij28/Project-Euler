'''
if the sum is divisible by some 3, number is divisible by 3, hence no permutation can be prime
1+2+3+4+5+6+7+8+9 = 45 # divisible by 3
1+2+3+4+5+6+7+8 = 36 # divisible by 3
1+2+3+4+5+6+7 = 28 # not divisible by 3 (check numbers)
1+2+3+4+5+6 = 21 # divisible by 3
1+2+3+4+5 = 15 # divisible by 3
1+2+3+4 = 10 not divisible by 3 (check numbers)
1+2+3 = 6 # divisible by 3
1+2 = 3 # divisible by 3
'''

from itertools import permutations
from math import sqrt

def isPrime(n):
	if n < 2: return False
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0: return False
	return True

pandigital_primes = []

four_digits = list(set([int("".join(i)) for i in permutations(["1", "2", "3", "4"])]))
seven_digits = list(set([int("".join(i)) for i in permutations(["1", "2", "3", "4", "5", "6", "7"])]))

numbers_to_check = four_digits + seven_digits

for i in numbers_to_check:
	if isPrime(i): pandigital_primes.append(i)
print max(pandigital_primes)
print isPrime(7654321)