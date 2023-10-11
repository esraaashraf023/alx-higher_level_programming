#!/usr/bin/python3
"""computing Pascal Triangle"""


def pascal_triangle(n):
    """function that represents the Pascal’s triangle"""
    pascal_list = [[]]
    new_row = []
    if n <= 0:
        return []
    pascal_list.append([1])

    for i in range(n - 1):
        middle_values = sum_index(new_row)
        new_row = [1] + middle_values + [1]
        pascal_list.append(new_row)

    return pascal_list[1:]


def sum_index(lst):
    """Calculate"""
    new_list = []
    for idx in range(0, len(lst) - 1):
        new_list.append(lst[idx] + lst[idx + 1])
    return new_list
