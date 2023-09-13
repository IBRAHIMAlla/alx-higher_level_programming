#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res = 0
    p = 0

    for c in reversed(roman_string):
        val = roman_numerals.get(c, 0)
        if val < p:
            res -= val
        else:
            res += val
        p = val

    return (res)
