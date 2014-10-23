#!/usr/bin/env python


def sum_even_fib(limit):
    fib_list = [1, 2]
    even_fib_list = [2]
    next_fib = fib_list[-1] + fib_list[-2]

    while(next_fib <= limit):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
        if next_fib % 2 == 0:
            even_fib_list.append(next_fib)

    return sum(even_fib_list)

print sum_even_fib(4*10**6)


def sum_even_fib(limit):
    even_fib_list = [2]
    last_fib = 2
    sec_last_fib = 1
    next_fib = last_fib + sec_last_fib

    while(next_fib <= limit):
        next_fib = last_fib + sec_last_fib
        sec_last_fib = last_fib
        last_fib = next_fib
        if last_fib % 2 == 0:
            even_fib_list.append(last_fib)

    return sum(even_fib_list)

print sum_even_fib(4*10**6)
