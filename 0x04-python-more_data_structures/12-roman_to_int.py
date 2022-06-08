#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            res += values[roman_string[i]]
        elif values[roman_string[i]] < values[roman_string[i + 1]]:
            res -= values[roman_string[i]]
        else:
            res += values[roman_string[i]]
    return res
