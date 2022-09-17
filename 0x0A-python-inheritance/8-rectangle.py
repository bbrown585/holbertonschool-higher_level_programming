#!/usr/bin/pyton3
"""Module for rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is descendent of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Rectangle init
        """
        self.integer_validator("width", width)
        self.__width = with
        self.integer_validator("height", height)
        self.__height = height
