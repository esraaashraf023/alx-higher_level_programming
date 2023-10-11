#!/usr/bin/python3
"""the function write_file"""


def write_file(filename="", text=""):
    """ that writes a string to a text file and returns the numb"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
