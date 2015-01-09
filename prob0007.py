#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
    if n == 1:
        return False
    for num in xrange(2, n):
        if n % num == 0:
            return False
    return True

def find_nth_prime(n):
    prime_count=0
    x=2
    while True:
        #print 'top', 'x is', x, 'prime_count', prime_count
        if is_prime(x):
            prime_count += 1
        if prime_count == n:
            break
        x += 1
        #print 'bot', 'x is', x, 'prime_count', prime_count
    return x


def find_nth_prime2(n):
    prime_count=0
    x=1
    while prime_count < n:
        x += 1
        if is_prime(x):
            prime_count += 1
    return x


def find_nth_prime3(n):
    prime_count=2
    x=3
    while prime_count < n:
        x += 2
        if is_prime(x):
            prime_count += 1
    return x


def find_nth_prime4(n):
    primes = [2]
    candidate = 3

    while len(primes) < n:
        is_composite = False
        for prime in primes:
            if candidate % prime == 0:
                is_composite = True
                break
        if not is_composite:
            primes.append(candidate)
        candidate += 2
    return primes[-1]


print find_nth_prime4(10001)

"""
next optimization to pursue:
do not check primes larger than sqrt of candidate
"""
