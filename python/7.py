"""Problem:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import sys

index = 0
primes_counted = 0
current_prime = 0

def isPrime(num):
    if num > 1:  
        for i in range(2, num): 
            if (num % i) == 0: 
                return False
        else: 
            return True 
    else: 
        return False

while primes_counted < 10001:

    index += 1

    if isPrime(index):

        primes_counted += 1
        current_prime = index


print(current_prime)