#!/usr/bin/python3
"""my list"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
