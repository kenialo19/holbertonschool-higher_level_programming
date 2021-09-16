#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == '':
        return None
    sum = 0
    dic_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    size_str = len(roman_string)
    for i in range(size_str):
        if i != size_str - 1 and (dic_roman[roman_string[i + 1]] > dic_roman[roman_string[i]]):
            sum -= dic_roman[roman_string[i]]
        else:
            sum += dic_roman[roman_string[i]]
    return sum
