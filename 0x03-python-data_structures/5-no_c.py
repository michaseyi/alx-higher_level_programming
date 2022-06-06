#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i in my_string:
        if i not in "cC":
            new_string.append(i)
    return "".join(new_string)
