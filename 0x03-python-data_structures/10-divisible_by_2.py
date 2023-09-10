#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listt = []
    for element in my_list:
        if element % 2 == 0:
            listt.append(True)
        else:
            listt.append(False)
    return listt
