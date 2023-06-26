#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        element = 0
        num_int = 0
        while (element < x):
            if isinstance(my_list[element], int):
                print("{:d}".format(my_list[element]), end="")
                num_int += 1
            element += 1
        print()
        return (num_int)
    except (TypeError, ValueError):
        print()

