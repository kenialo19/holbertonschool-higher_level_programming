#!/usr/bin/env python3
def uppercase(str):
    ln = len(str)
    for i in range(ln):
        if ord(str[i]) in range(97, 123):
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{:c}".format(ord(str[i])), end='')
    print()
