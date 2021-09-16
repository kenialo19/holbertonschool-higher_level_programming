#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a,b = 0,0
    lengi = len(my_list)
    for i in range(lengi):
        a += my_list[i][0] * my_list[i][1]
        b += my_list[i][1]
    return(a / b)
