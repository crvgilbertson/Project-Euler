# Problem: A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagoreanTriple():
	hypotenuse = 1000
	for a in range(1, hypotenuse + 1):
		for b in range(a + 1, hypotenuse + 1):
			c = hypotenuse - a - b
			if a * a + b * b == c * c:
				return str(a * b * c)

print(pythagoreanTriple())
