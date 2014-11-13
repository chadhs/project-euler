#!/usr/bin/env python

"""
find 3 numbers that add up to 1000
that are also a pythagorean triplet

iterate through a list of sum sets checking with is_py_trip helper function

return the product of a b & c
"""

def is_py_trip(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def find_py_trip(ptsum):
    for aval in range(1, (ptsum / 3)):
        for bval in range(aval + 1, ptsum):
            cval = ptsum - aval - bval
            check = is_py_trip(aval, bval, cval)
            #print aval, bval, cval, 'is', check
            if check:
                return aval * bval * cval
            bval += 1
        aval += 1


print find_py_trip(1000)
