#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("is positive: {:d}".format(number))

elif number == 0:
    print("is zero: {:d}".format(number))
    
else:
     print("is negative: {:d}".format(number))
