#!/usr/bin/python3
"""List Module"""


class MyList(list):
    """MyList class list"""
    def print_sorted(self):
        """Print List"""
        print(sorted(self))
