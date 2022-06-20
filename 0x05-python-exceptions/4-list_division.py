#!/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            res_list.append(res)
    return res_list
