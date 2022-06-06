#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = float('-inf')
    for number in my_list:
        if number > max:
            max = number
    return max
