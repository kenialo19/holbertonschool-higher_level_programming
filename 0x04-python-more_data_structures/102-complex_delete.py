#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = list(a_dictionary.keys())
    y = list(a_dictionary.values())
    for i, key in enumerate(x):
        if value is y[i]:
            del a_dictionary[key]
    return a_dictionary
