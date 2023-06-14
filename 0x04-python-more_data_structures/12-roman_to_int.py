#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    result = number = 0

    if (type(roman_string) is not str) or (roman_string is None):
        return (0)

    for c in reversed(roman_string):
        value = roman_numbers[c]
        if value >= number:
            result += value
        else:
            result -= value

        number = value
    return (result)
