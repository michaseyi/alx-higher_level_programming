#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictionary.keys())
    new_list.sort()
    for keys in new_list:
        print("{}: {}".format(keys, a_dictionary[keys]))
