#!/usr/bin/env python


def multiple_sum(max):
    sum = 0

    for num in range(max):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    return sum

print multiple_sum(1000)


def multiple_sum(max):
    list_of_multiples = []

    for num in range(max):
        if num % 3 == 0 or num % 5 == 0:
            list_of_multiples.append(num)

    return sum(list_of_multiples)

print multiple_sum(1000)


def multiple_sum(max):
    multiples = [num for num in range(max) if num % 3 == 0 or num % 5 == 0]
    return sum(multiples)


print multiple_sum(1000)


def multiple_sum(max):

    list_of_3s = range(0, 1000, 3)
    list_of_5s = range(0, 1000, 5)
    list_of_15s = range(0, 1000, 15)

    return sum(list_of_3s + list_of_5s) - sum(list_of_15s)


print multiple_sum(1000)
