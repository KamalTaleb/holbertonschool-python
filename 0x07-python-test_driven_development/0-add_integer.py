#!/usr/bin/python3
"""kamal"""


def add_integer(a, b=98):
    """kamal"""
    fnum = 0
    if type(a) is int or type(a) is float:
        fnum += int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        fnum += int(b)
    else:
        raise TypeError("b must be an integer")
    return fnum
