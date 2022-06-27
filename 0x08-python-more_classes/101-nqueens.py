#!/usr/bin/python3
"""This module defines a function nqueen that solves the famouse nqueen
   problem
"""


def nqueen(track=[], start=0):
    """
    nqueen finds all possible position to place n queens on a n by n chess
    board where each queen is not in an attaking position.

    This function prints out the possible arrangements to the standard output

    :param track(list): used for backtracking and holding the position
    leading to the current recursive call
    :param start(int): is the current index of the present recursive call
    """
    if start == n:
        print(track)
        return

    for i in range(n):
        col_val = i
        pos_dig_val = start + i
        neg_dig_val = start - i
        if col_val in col or pos_dig_val in pos_dig or neg_dig_val in neg_dig:
            continue
        else:
            col.add(col_val)
            pos_dig.add(pos_dig_val)
            neg_dig.add(neg_dig_val)
            track.append([start, i])
            nqueen(track, start + 1)
            track.pop()
            col.remove(col_val)
            pos_dig.remove(pos_dig_val)
            neg_dig.remove(neg_dig_val)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    col = set()  # holds the  column posistion of a placed queen
    pos_dig = set()  # holds the positive diagonal of a placed queen
    neg_dig = set()  # holds the negative diagonal of a placed queen\
    nqueen()
