#!/usr/bin/python3
def reverse_alpha():
    for i in range(90, 64, -1):
        if (i % 2) == 0:
            i = i + 32
        print(f"{chr(i)}", end="")


if __name__ == "__main__":
    reverse_alpha()
