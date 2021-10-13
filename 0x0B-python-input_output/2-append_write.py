#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
