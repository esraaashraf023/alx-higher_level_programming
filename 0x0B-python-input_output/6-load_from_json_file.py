#!/usr/bin/python3
"""the function"""


import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)
