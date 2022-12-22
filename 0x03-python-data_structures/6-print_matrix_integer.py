#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers'''
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            print("{}".format(matrix[i][x]), end=" ")
            if len(matrix[x]) != len(matrix[i]):
                print(" ", end="")
        print("")
