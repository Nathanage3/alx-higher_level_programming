#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num enumerate(row):
            if i != len(row) - 1:
                print("{:d}".format(i))
            else:
                print("{:d}".format(num))
        print()
