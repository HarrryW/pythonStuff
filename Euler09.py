"""Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""



def pythagChecker(a,b,c):
	if a**2+b**2==c**2 and a<b<c:
		return True
	return False
def main():
	i = 0
	x = 0
	for n in xrange(3,1000):
		for z in xrange(4,1000):
				for y in xrange(5,1000):
					if pythagChecker(n,z,y) and n+z+y==1000:
						print n, z, y
					else:
						continue
					
main()

#nothing new from this one, im sure there's a simpler way to solve it instead of using 3 seperate ranges