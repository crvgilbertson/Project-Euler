# Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001st prime number?

import eulerlib, itertools, sys

def highPrime():
	hprime = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
	return hprime


print(highPrime())