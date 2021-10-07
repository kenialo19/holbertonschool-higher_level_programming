#!/usr/bin/python3
"""
Print a text with 2 new lines after
each of these characters
. ? :
"""


def text_indentation(text):

    flag = True
    delimiters = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and flag is True:
            continue

        if i in delimiters:
            print("{}".format(i), end="")
            print("\n")
            flag = True
        else:
            print(i, end="")
            flag = False
