#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) in range(97, 123):
            caps = chr(ord(s) - 32)
        else:
            caps = s
        print("{}".format(caps), end="")
    print("")
