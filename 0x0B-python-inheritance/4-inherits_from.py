#!/usr/bin/python3
"""inherets from"""


def inherits_from(obj, a_class):
    """
    inherets from
    """
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        else:
            return True
    else:
        return False
