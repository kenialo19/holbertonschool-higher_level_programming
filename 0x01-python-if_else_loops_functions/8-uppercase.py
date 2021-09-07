#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        ptr = ord(i)
        if (ptr >= 97 and ptr <= 122):
            ptr -= 32
        print("{:c}".format(ptr), end='')
    print()
