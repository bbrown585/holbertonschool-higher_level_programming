#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """append a string at then end and return number"""
    with open(filename, "a", encoding="utf-8") as content:
        return content.write(text)
