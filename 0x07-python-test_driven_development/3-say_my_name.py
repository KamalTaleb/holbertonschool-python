#!/usr/bin/python3
"""kamal"""


def say_my_name(first_name, last_name=""):
    """kamal"""
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
