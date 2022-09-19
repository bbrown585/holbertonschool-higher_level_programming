#!/usr/bin/pyton3
"""Object from JSON file module"""
import json


def load_from_json_file(filename):
    """creates an Ojbect from JSON file"""
    with open(filename, "r", encoding="utf-8") as content:
        return json.load(content)
