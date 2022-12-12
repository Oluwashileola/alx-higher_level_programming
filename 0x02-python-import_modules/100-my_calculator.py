#!/usr/bin/python3

if __name__ == "__main__":
    '''adds, subtracts, multiplies and divides two numbers'''
    from calculator_1 import add, sub, mul, div
    import sys

    arg_error_message = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    operator_error_message = "Unknown operator. Available operators: +, -, * and /"

    if (len(sys.argv) - 1) != 3:
        print("{}".format(arg_error_message))
        sys.exit(1)
    else:
        a = int(sys.argv[0 + 1])
        b = int(sys.argv[2 + 1])
        operator = sys.argv[1 + 1]

        if operator == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        elif operator == "-":
            print("{} - {} = {}".format(a, b, sub(a, b))
            sys.exit(0)
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b))
            print(0)
        elif operator == "/":
            print("{} / {} = {}".format(a, b, div(a, b))
            sys.exit(0)
        else:
            print("{}".format(operator_error_message))
            sys.exit(1)
