#!/usr/bin/env python

from math import sqrt


def lg_prime_factor(number):
    factor_list = []
    prime_list = []
    for num in range(2, number + 1):
        if number % num == 0:
        # if number % num == 0 and num % 2 != 0:
            factor_list.append(num)
    # print 'factors of ' + str(number) + ' are ' + str(factor_list)

    """
    for each of the factors in the factor list
       if it is not divisible by another factor then add it to a prime list
    """

    divisor_list = factor_list

    for factor in factor_list[::-1]:
        factor_count_list = []
        for divisor in divisor_list:
            if divisor <= factor:
                if factor % divisor == 0:
                    factor_count_list.append(factor)
        if len(factor_count_list) <= 2:
            prime_list.append(factor)

    print 'prime factors of ' + str(number) + ' are ' + str(prime_list)
    print 'largest prime factor of ' + str(number) + ' is ' + str(prime_list[0])


lg_prime_factor(60)
# lg_prime_factor(60085147)
# lg_prime_factor(600851475143)


def lg_prime_factor(number):
    factor_list = []
    prime_list = []
    for num in range(2, int(sqrt(number + 1))):
        if number % num == 0:
        # if number % num == 0 and num % 2 != 0:
            factor_list.append(num)
    # print 'factors of ' + str(number) + ' are ' + str(factor_list)

    """
    for each of the factors in the factor list
       if it is not divisible by another factor then add it to a prime list
    """

    divisor_list = factor_list

    for factor in factor_list[::-1]:
        factor_count_list = []
        for divisor in divisor_list:
            if divisor <= factor:
                if factor % divisor == 0:
                    factor_count_list.append(factor)
        if len(factor_count_list) <= 2:
            prime_list.append(factor)

    print 'prime factors of ' + str(number) + ' are ' + str(prime_list)
    print 'largest prime factor of ' + str(number) + ' is ' + str(prime_list[0])

lg_prime_factor(600851475143)


def lg_prime_factor(number):
    n = number
    factor = 2  # we're only checking for factors greater than last factor
    lastfactor = 1  # we'll start with the smallest factor
    while n > 1:
        """
        if our number is cleanly divisible by our current factor then it
        becomes our last factor (current largest factor).

        since n is divisble by something other than 1 and itself the new
        limit becomes n / factor (we're looking for primes not all factors)

        increment factor by 1 and continue the loops till n / factor = 1
        and return the last factor which will be the greatest prime
        """
        if n % factor == 0:
            lastfactor = factor
            n = n / factor
            # while n % factor == 0:
                # n = n / factor
        factor = factor + 1
    return lastfactor

print lg_prime_factor(600851475143)
