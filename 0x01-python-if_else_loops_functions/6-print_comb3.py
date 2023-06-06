#!/usr/bin/python3
for i in range(9):
    for d in range(1, 10):
        if (i != d and i < d and i < 8):
            print("{:d}{:d}".format(i, d), end=", ")
print("{:d}{:d}".format(i, d), end="\n")
