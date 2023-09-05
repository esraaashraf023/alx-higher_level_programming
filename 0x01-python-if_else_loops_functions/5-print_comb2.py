#!/usr/bin/pytho
for k in range (100):
    if k == 99:
        print("{:d}".format(k))
    else:
        print("{:d}".format(k).zfill(2), end=' , ')
