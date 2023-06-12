#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for element in list:
            if element != list[-1]:
                print("{:d}".format(element), end=' ')
            else:
                print("{:d}".format(element), end='')
        print("")
