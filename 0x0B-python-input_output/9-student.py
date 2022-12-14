#!/usr/bin/python3
"""JSON student module"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return Student"""
        return self.__dict__
