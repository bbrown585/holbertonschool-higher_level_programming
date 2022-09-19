#!/usr/bin/python3
"""JSON module"""


def class_to_json(obj):
    """returns the dictionary"""
    return obj.__dict__
