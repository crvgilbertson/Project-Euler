# Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import eulerlib

def sum_of_primes():
    x = sum(eulerlib.primes(1999999))
    return x

print(sum_of_primes())
