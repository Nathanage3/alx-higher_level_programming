#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    for numeral in reversed(roman_string):
        value = roman_dict.get(numeral, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
