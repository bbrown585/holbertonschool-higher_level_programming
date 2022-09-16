#!/usr/bin/python3
"""Class Module"""


class BaseGeometry():
    """create a class"""
    def area(self):
        """method to calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method to validate value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
