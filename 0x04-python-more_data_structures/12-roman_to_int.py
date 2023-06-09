#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_string = roman_string.upper()
    num = []
    result = 0
    prev = 0
    roman_num = {'I': 1, 'V': 5,
                 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for item in roman_string:
        for key, value in roman_num.items():
            if item == key:
                num.append(value)
    ln = len(num)
    for i in num:
        nex = i
        if prev < nex:
            new = nex - prev - prev
            result += new
        else:
            result += i
        prev = i

    return result
