#!/usr/bin/python3
"""create class rectangle"""
from models.base import Base
 


class Rectangle(Base):
    """init class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height porperty"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x axis"""
        return self.__x

    @x.setter
    def x(self, value):
        """x axis"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y axis"""
        return self.__y

    @y.setter
    def y(self, value):
        """y axis"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area"""
        return (self.width * self.height)

    def __str__(self):
        """overriding str"""
        a, b, c, d, e = self.id, self.x, self.y, self.width, self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def display(self):
