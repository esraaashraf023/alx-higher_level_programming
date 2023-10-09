#!/usr/bin/python3
"""For lookup function"""


def lookup(obj):
    """
    Returns a list object.

    Args:
        obj: The object to inspect.
    """
    return list(dir(obj))
