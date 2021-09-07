#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        ptr = ord(i)
        if ptr in range(97, 123):
            ptr -= 32
        print("{:c}".format(ptr), end='')
    print()
