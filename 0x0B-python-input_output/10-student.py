#!/usr/bin/python3
"""Student class define modul"""


class Student():
    """create class"""
    def __init__(self, first_name, last_name, age):
        """defines a student by attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Returnsstudents"""
        if type(attr) is not list:
            return(self.__dict__)
        if (not all(isinstance(items, str) for items in attr)):
            return(self.__dict__)
        result = {}
        return({key: self.__dict__[key] for
                key in self.__dict__.keys() & attr})
