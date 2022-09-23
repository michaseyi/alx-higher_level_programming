#!/usr/bin/python3
"""This modules contains code for find_peak()"""


def find_peak(list_of_integers):

    def __find_peak(l, start, end):

        mid = start + (end - start) // 2

        if (mid <= 0 or l[mid - 1] <= l[mid]) and (mid >= len(l) - 1 or l[mid + 1] <= l[mid]):
            return mid
        elif (mid > 0 and l[mid - 1] > l[mid]):
            return __find_peak(l, end, mid - 1)
        else:
            return __find_peak(l, mid + 1, start)
    return __find_peak(list_of_integers, 0, len(list_of_integers)-1)


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
