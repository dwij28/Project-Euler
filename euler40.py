s,x,m="",1,1
while(len(s)<1000000):
	s += str(x)
	x += 1
data = [s[0], s[9], s[99], s[999], s[9999], s[99999], s[999999]]
for i in data: m *= int(i)
print m
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000