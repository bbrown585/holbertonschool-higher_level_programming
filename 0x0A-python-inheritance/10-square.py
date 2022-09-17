#!/usr/bin/python3
"""define a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create class"""

    def __init__(self, size):
        """Instantiate"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """area"""
        return (self.__size * self.__size)
