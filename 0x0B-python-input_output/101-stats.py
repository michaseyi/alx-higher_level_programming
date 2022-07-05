#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""

line_count = 0
total_file_size = 0
t = table = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
             405: 0, 500: 0}


def print_stat():
    """
    print_stat prints the stat of the the metrics processed after
    reading 10 lines
    """
    print("File size: {}".format(total_file_size))
    sorted_list = table.keys()
    for key in sorted_list:
        if table[key] > 0:
            print("{}: {}".format(key, table[key]))


try:
    from sys import stdin
    for line in stdin:
        if line_count % 10 == 0 and line_count > 0:
            print_stat()
        line = line.split()
        total_file_size += int(line[8])
        if int(line[7]) in table.keys():
            table[int(line[7])] += 1
        line_count += 1
except KeyboardInterrupt:
    print_stat()
    raise
