#!/usr/bin/env python3
def uppercase(str):
    ln = len(str)
    for i in range(0, ln):
        if str[i] >= 'a' and str[i] <= 'z':
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{:c}".format(ord(str[i])), end='')
    print()
