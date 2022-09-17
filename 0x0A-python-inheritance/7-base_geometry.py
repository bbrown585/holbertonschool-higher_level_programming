#!/usr/bin/python3
"""class"""


class BaseGeometry():
    """create class"""
    pass

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if (type(value) is not int):
            raise TypeError(str(name) + " must be an integer")
        if (value <= 0):
            raise ValueError(str(name) + " must be greater than 0")
