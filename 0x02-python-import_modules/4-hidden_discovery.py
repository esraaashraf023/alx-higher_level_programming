#!/usr/bin/python3
import sys
if _name_ == "_main_":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[0:2]="__":
            print(name)
