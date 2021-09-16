#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    dic_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    size_str = len(roman_string)
    for i in range(size_str):
        if roman_string[i] in dic_roman:
            sum += dic_roman[roman_string[i]]
    return sum
