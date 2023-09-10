#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for k in my_string:
        if k != 'c' and k != 'C':
            new_string += k
    return new_string
