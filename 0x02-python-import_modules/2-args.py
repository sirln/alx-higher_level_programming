#!/usr/bin/python3

import sys


def print_args(args):
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
        sys.exit(0)

    add_s = 's' if num_args > 1 else ''
    print("{} argument{}:".format(num_args, add_s))

    if num_args != 0:
        for i, arg in enumerate(args):
            print(f"{i + 1:d}: {arg}")


if __name__ == "__main__":
    print_args(sys.argv[1:])
