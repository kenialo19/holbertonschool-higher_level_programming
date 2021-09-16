#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dup_dic = a_dictionary.copy()
    for i in dup_dic:
        dup_dic[i] *= 2
    return dup_dic
