#!/usr/bin/python3
def element_at(my_list, idx):
    list_lengthe = len(my_list) -1
    if (idx < 0 or idx >= list_lengthe):
        return None
    else:
        return my_list[idx]
