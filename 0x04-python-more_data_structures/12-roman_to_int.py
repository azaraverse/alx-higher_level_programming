#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    values = list(map(lambda x: numerals.get(x, 0), roman_string))

    for i in range(len(roman_string) - 1):
        if values[i] < values[i + 1]:
            values[i] = -values[i]
    return sum(values)
