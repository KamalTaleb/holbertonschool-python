#!/usr/bin/python3
"""kamal"""


def print_square(size):
    """kamal"""
    if type(size) is int:
        if size >= 0:
            for iter in range(size):
                for iter2 in range(size):
                    print("#", end="")
                print("")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
