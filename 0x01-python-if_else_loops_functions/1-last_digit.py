#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if ((number % 10) == 0):
    print("{:d} and is 0".format(number))
elif ((number % 10) > 5):
    print("{:d} and is greater than 5".format(number))
else:
    print("{:d} and is less than 6 and not 0".format(number))
