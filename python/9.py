"""
Problem:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def square(num):
    return num*num

for a in range (1000):

    for b in range (1000):

        for c in range (1000):

            if (square(a) + square(b) == square(c)) and (a + b + c == 1000):

                print(a*b*c)

