"""
Problem:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

number = 2000001
is_prime = [1]*number
is_prime[0] = 0
is_prime[1] = 0

primes_sum = 0

def sieve():
    i = 2
    while i*i <= number:
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < number:
            is_prime[j] = 0
            j += i

        i += 1

sieve()
for i in range(1, number):
    if is_prime[i] == 1:
        primes_sum += i

print(primes_sum)
