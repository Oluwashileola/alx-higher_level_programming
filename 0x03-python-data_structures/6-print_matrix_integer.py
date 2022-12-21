#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers'''
    if isinstance(matrix, (list, int)):
        if matrix == [[]]:
            print("")
        else:
            for i in matrix:
                for x in i:
                    print("{}".format(x), end=" ")
                print("")
    return None
