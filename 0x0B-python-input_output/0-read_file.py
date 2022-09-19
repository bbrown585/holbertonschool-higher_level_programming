#!/usr/bin/python3
"""Stdout module"""


def read_file(filename=""):
    """something about the funtion goes here b"""

    with open(filename, "r") as a_list:
        print(a_list.read(), end="")
        a_list.close()
