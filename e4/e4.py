"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

>>> import os
>>> largest_palindrome_product_of_n_digit_numbers(2)
9009
>>> str(largest_palindrome_product_of_n_digit_numbers(3)) == os.getenv("EULER4")
True
>>> str(largest_palindrome_product()) == os.getenv("EULER4")
True
"""

from itertools import combinations_with_replacement as cwr


def largest_palindrome_product_of_n_digit_numbers(n):
    return max(
        comb
        for x, y in cwr(range(10 ** (n - 1) + 1, 10 ** n), r=2)
        if str((comb := x * y)) == str(comb)[::-1]
    )


def largest_palindrome_product():
    best = 0
    for i in range(990, 100, -11):  # A 6-digit palindromic number is a multiple of 11
        for j in range(999, 100, -1):
            n = i * j
            if n < best:
                break
            if str(n) == str(n)[::-1]:
                best = max(best, n)
    return best


if __name__ == "__main__":
    print(largest_palindrome_product())
