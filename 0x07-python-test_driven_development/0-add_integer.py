#!/usr/bin/python3
"""
This module has a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Returns:
        The addition of the two given numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
