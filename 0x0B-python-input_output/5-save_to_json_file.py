#!/usr/bin/python3
""" the function"""


import json


def load_from_json_file(filename):
    """that writes an Object to a text file"""
    with open(filename, 'r') as file:
        return json.load(file)
