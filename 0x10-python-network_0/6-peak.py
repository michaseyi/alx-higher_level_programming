#!/usr/bin/python3
"""This modules contains code for find_peak()"""


def find_peak(list_of_integers):
    """
    find_peak finds a peak number from a list of integers

    :param list_of_integers(list[int]): is the list to retrieve peak from
    :return: is the peak
    """
    def __find_peak(vals, start, end):
        """
        __find_peak performs binary search to find peak value
        """
        if len(vals) < 1:
            return None
        mid = start + (end - start) // 2
        if (mid <= 0 or vals[mid - 1] <= vals[mid]) and (
                mid >= len(vals) - 1 or vals[mid + 1] <= vals[mid]):
            return vals[mid]
        elif (mid > 0 and vals[mid - 1] > vals[mid]):
            return __find_peak(vals, start, mid-1)
        else:
            return __find_peak(vals, mid+1, end)
    return __find_peak(list_of_integers, 0, len(list_of_integers)-1)
