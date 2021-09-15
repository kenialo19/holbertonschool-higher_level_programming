#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list.copy()
    for i, idx in enumerate(list):
        if idx is search:
            list[i] = replace
    return list