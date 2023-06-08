#!/usr/bin/python3

import sys


def infinite_addition(args):
    num_args = len(args)
    sum = 0

    if num_args == 0:
        print(0)
        sys.exit(0)

    for arg in args:
        sum += int(arg)
    print(sum)


if __name__ == "__main__":
    infinite_addition(sys.argv[1:])
