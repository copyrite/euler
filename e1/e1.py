"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

>>> import os
>>> sum_of_multiples_of_3_or_5(10)
23
>>> str(sum_of_multiples_of_3_or_5(1000)) == os.getenv("EULER1")
True
>>> str(sum_of_multiples(1000, (3, 5))) == os.getenv("EULER1")
True
>>> str(sum(i for i in range(1000) if (not i % 3 or not i % 5))) == os.getenv("EULER1")
True
>>> str(sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5)))) == os.getenv("EULER1")
True
"""

from functools import reduce
from itertools import chain, combinations
from math import gcd
from operator import mul


def sum_of_multiples_of_3_or_5(bound):
    """
    Sum of integers below `bound` that are multiples of 3 or 5.
    """
    poly = lambda x: (x * (x + 1))
    return sum(x * poly((bound - 1) // abs(x)) for x in (3, 5, -15)) // 2


def sum_of_multiples(bound, multiples):
    """
    Sum of integers below `bound` that are multiples of any integer in
    the sequence `multiples`.

    Uses inclusion-exclusion principle with sums of arithmetic sequences.
    """

    total = 0
    for subset in chain.from_iterable(
        combinations(multiples, r) for r in range(1, len(multiples) + 1)
    ):
        # LCM of an arbitrary set of integers
        lcm = reduce(lambda x, y: mul(x, y) // gcd(x, y), subset)
        bnd = (bound - 1) // lcm
        total += (2 * (len(subset) % 2) - 1) * lcm * bnd * (1 + bnd) // 2
    return total


if __name__ == "__main__":
    print(sum_of_multiples_of_3_or_5(1000))
