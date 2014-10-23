#!/usr/bin/env python

from operator import mul


def find_smallnum(num):
    toobig = reduce(mul,range(1,num),1)

    for i in xrange(num, toobig + 1):
        numcheck = True
        for j in range(2, num + 1):
            if i % j != 0:
                numcheck = False

        if numcheck:
            return i

#print find_smallnum(20)
print find_smallnum(8)





"""
13
a 13
12 = 3x2x2
a 13x3x2x2
11
a 13x3x2x2x11
10 = 2x5
a 13x3x2x2x11x5
9 = 3x3
a 13x3x2x2x11x5x3
8 = 2x2x2
a 13x3x2x2x11x5x3x2
7
a 13x3x2x2x11x5x3x2x7
6 = 2x3
a 13x3x2x2x11x5x3x2x7
4 = 2x2
a 13x3x2x2x11x5x3x2x7
"""
