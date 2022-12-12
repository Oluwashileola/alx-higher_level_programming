#!/usr/bin/python3

if __name__ == "__main__":
    '''adds, subtracts, multiplies and divides two numbers'''
    import calculator_1, sys

    arg_error_message = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    operator_error_message = "Unknown operator. Available operators: +, -, * and /"


    if len(sys.argv) != 3:
        print("{}".format(arg_error_message))
        print(1)
    else:
        a = int(sys.argv[0 + 1])
        b = int(sys.argv[2 + 1])
        operator = sys.argv[1 + 1]

        if operator == "+":
            print(calculator_1.add(a, b))
            print(0)
        elif operator == "-":
            print(calculator_1.sub(a, b))
            print(0)
        elif operator == "*":
            print(calculator_1.mul(a, b))
            print(0)
        elif operator == "/":
            print(calculator_1.div(a, b))
            print(0)
        else:
            print("{}".format(operator_error_message))
            print(1)
