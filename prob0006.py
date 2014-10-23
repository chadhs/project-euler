#!/usr/bin/env python

"""
take the sum of the squares of the natural numbers 1 to n
take the square of the sum of the natural numbers 1 to n
return the difference of the sum of squares and square of the sum of n
"""

def sum_squares(n):
    sumsq = 0
    for num in range(1, n+1):
        sumsq += num ** 2
    return sumsq

def square_sum(n):
    sqsum = sum(range(1, n+1)) ** 2
    return sqsum

def diff_sqsum_sumsq(n):
    return square_sum(n) - sum_squares(n)

print diff_sqsum_sumsq(100)
