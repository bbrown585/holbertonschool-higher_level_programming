#!/usr/bin/python3
"""string to text module"""


def write_file(filename="", text=""):
    """function that writes a string to a txt (UTF8)"""
    with open(filename, "w", encoding="utf-8") as content:
        return content.write(text)
