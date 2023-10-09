#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class"""

    def area(self):
        """Tthe geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value is not an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
