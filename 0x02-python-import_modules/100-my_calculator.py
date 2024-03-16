#!/usr/bin/python3
if __name__ == "__main__":

import sys
from calculator_1 import add, subtract, multiply, divide

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    operator = sys.arg[2]
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, add(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, add(a, b)))
     elif operator == "/":
        print("{} / {}= {}".format(a, b, add(a, b)))
    else:
        print("Unknown operator. Availabe operators: +, -, * and /")
        exit(1)

