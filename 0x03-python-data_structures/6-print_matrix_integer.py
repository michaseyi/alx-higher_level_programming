#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            print()
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end="\n" if j ==
                  len(matrix[i]) - 1 else " ")
