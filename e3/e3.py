"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

>>> import os
>>> [largest_factor(x) for x in range(21)]
[0, 1, 2, 3, 2, 5, 3, 7, 2, 3, 5, 11, 3, 13, 7, 5, 2, 17, 3, 19, 5]
>>> largest_factor(2*2*3*5*7)
7
>>> str(largest_factor(600851475143)) == os.getenv("EULER3")
True
"""

from itertools import chain
from itertools import count


def prime_candidates():
    return chain(
        (2, 3, 5),
        (big + med for big in count(0, 30) for med in (7, 11, 13, 17, 19, 23, 29, 31)),
    )


def largest_factor(n):
    for d in prime_candidates():
        dsq = d ** 2
        if dsq > n:
            break
        while dsq <= n and not n % d:
            n = n // d
    return n


if __name__ == "__main__":
    print(largest_factor(600851475143))
