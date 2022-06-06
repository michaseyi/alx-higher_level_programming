#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret_val = []
    for number in my_list:
        if number % 2 == 0:
            ret_val.append(True)
        else:
            ret_val.append(False)
    return ret_val
