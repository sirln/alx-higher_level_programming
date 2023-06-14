#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)
    score = sum(map(lambda tuple: tuple[0] * tuple[1], my_list))
    weight = sum(map(lambda tuple: tuple[1], my_list))
    weighted_average = float(score/weight)
    return (weighted_average)
