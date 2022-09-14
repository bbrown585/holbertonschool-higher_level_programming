#!/usr/bin/python3
"""Create rectangle module"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Initialize Rectangle width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Initialize Rectangle height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """return rectangle"""
        print_rec = ""
        if self.__width > 0 and self.__height > 0:
            for idx in range(self.__height):
                print_rec += "#" * self.__width
                print_rec += "\n"
            print_rec = print_rec[:-1]
        return print_rec

    def __repr__(self):
        """ return rectangle"""
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'
