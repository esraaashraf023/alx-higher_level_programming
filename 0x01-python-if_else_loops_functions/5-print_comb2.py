#!/usr/bin/pytho3
for r in range(100):
    if r == 99:
        print("{:d}".format(r))
    else:
        print("{:d}".format(r).zfill(2), end=", ")

