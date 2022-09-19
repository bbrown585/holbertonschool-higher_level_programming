#!/usr/bin/python3
"""json module for structure"""
import json


def from_json_string(my_str):
    """returns the JSON (string)"""
    return json.loads(my_str)
