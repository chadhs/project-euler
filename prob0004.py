#!/usr/bin/env python

from timeit import timeit


def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


def get_products():  # lists and sorting method
    products = []
    palindromes = []

    for num in range(100, 1000):
        for num2 in range(100, 1000):
            products.append(num * num2)

    for product in products:
        if is_palindrome(product):
            palindromes.append(product)

    palindromes.sort()
    return palindromes[-1]


print get_products()
print 'runtime = ' + str(timeit(get_products, number=1))


def get_products():  # on the fly check with no lists, update value
    max_palindrome = 0

    for num in range(100, 1000):
        for num2 in range(100, 1000):
            p = num * num2
            if is_palindrome(p):
                if p > max_palindrome:
                    max_palindrome = p

    return max_palindrome


print get_products()
print 'runtime = ' + str(timeit(get_products, number=1))


"""
idea start with the largest numbers and as soon as you find a palindrome
stop and return the value.
"""


def get_products():  # start ranges high, break after finding smaller result
    max_palindrome = 0

    for num in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            p = num * num2
            if is_palindrome(p):
                if p < max_palindrome:
                    break
                else:
                    max_palindrome = p
        else:
            continue

    return max_palindrome


print get_products()
print 'runtime = ' + str(timeit(get_products, number=1))


def get_products():  # start ranges high, break after finding smaller result
    max_palindrome = 0

    for num in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            p = num * num2
            if p < max_palindrome:
                break
            if is_palindrome(p):
                max_palindrome = p

    return max_palindrome


print get_products()
print 'runtime = ' + str(timeit(get_products, number=1))
