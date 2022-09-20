#!/usr/bin/python3
"""Student class module"""


class Student():
    """defines a Student class"""
    def __init__(self, first_name, last_name, age):
         """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return Student"""
        return self.__dict__.copy()
