#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_my_list = my_list.copy()
    if idx < 0:
        return cpy_my_list
    if idx >= len(my_list):
        return cpy_my_list
    cpy_my_list[idx] = element
    return cpy_my_list
