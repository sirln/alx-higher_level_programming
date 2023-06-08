#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def my_calculator(args):
    num_args = len(args)

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = args[1]
    a = int(args[0])
    b = int(args[2])

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    else:
        print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    my_calculator(sys.argv[1:])
