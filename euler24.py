from itertools import permutations as p
x = "0123456789"
print "".join(list(p(x))[999999])