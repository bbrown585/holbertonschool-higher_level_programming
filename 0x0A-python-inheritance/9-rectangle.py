#!/usr/bin/python3
"""define a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create a class"""

    def __init__(self, width, height):
        """width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __str__(self):
        """width and height"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
