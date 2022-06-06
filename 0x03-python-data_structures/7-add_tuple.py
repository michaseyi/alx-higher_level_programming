#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = (0 if not len(
        tuple_a) > 0 else tuple_a[0])+(0 if not (len(tuple_b) >
                                                 0) else tuple_b[0])
    b = (0 if not len(
        tuple_a) > 1 else tuple_a[1])+(0 if not (len(tuple_b) >
                                                 1) else tuple_b[1])
    return (a, b)
