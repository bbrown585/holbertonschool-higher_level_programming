#!/usr/bin/python3
"""Object instance of class Module"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an instance of the same class
    """
    if type(obj) is a_class:
        return True
    return False
