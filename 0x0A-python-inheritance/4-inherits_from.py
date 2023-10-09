#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
        of a class that inherited
        ; otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
