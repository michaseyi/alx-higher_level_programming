#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for keys in new_dict.keys():
        new_dict[keys] *= 2
    return new_dict
