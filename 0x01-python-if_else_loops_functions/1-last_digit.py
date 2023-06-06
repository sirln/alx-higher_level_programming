#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    return (number - (10 * int(number / 10)))


num = last_digit(number)
if (num > 5):
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
elif (num < 6 and num != 0):
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {num:d} and is 0")
