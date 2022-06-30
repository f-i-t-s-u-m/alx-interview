#!/usr/bin/env python3
""" python file with one function """


def minOperations(n):
    """ make min operation function """
    x, y, d = 0, n, 0
    while d <= y:
        if (d not in [0, 1] and y % d == 0):
            x = x + d
            y = y / d
            d = 0
        d += 1

    return x
