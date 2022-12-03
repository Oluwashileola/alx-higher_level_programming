#!/usr/bin/python3

'''Write a program that prints numbers from 0 to 99 seperated by a comma.'''

for num in range(0, 100):
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num)
