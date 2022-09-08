#!/usr/bin/python3
"""Create class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize Square"""
        self.__size = size
        """if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")"""

    def area(self, area=0):
        """defines area"""
        return(self.__size * self.__size)

    @property
    def size(self):

        """ define size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define area"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
