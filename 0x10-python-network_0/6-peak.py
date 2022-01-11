#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    else:
        v = len(list_of_integers)
        list_of_integers.sort()
        max_value = list_of_integers[v-1]
        return (max_value)
