#!/usr/bin/python3
"""Create class"""


class Square:
    """Square class """
    def __init__(self, size=0):
        """Initialize Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
