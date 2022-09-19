#!/usr/bin/python3
"""write an Object module"""
import json



def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON"""
    with open(filename, "w", encoding="utf=8") as content:
        json.dump(my_obj, content)
