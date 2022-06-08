#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    total_weight = 0
    for i in my_list:
        sum += i[0] * i[1]
        total_weight += i[1]
    return sum / total_weight
