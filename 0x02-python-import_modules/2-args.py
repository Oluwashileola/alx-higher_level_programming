#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    num = len(sys.argv) - 1
    if num == 0:
        print("{} arguments.")
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))

    for i in range(0, num):
        print("{}: {}".format(i + 1, sys.argv[i]))
