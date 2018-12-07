# This problem has an image, so you may view it here:
# https://projecteuler.net/problem=15

import eulerlib
import math

def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def mrSolveIt():
	return str(binomial(40, 20))

print(mrSolveIt())
