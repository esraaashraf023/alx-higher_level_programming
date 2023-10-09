#!/usr/bin/python3
"""for MyList class"""


class MyList(list):
    """Subclass from list"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
