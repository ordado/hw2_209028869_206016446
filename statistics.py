import math


def sum(values):
    s = 0
    for value in values:
        s += value
    return s


def mean(values):
    s = sum(values)
    return s / len(values)


def median(values):
    values.sort()
    len_of_values = len(values)
    if len_of_values % 2 == 0:
        len_of_values = int(len_of_values / 2) - 1
        return (values[len_of_values] + values[len_of_values + 1]) / 2
    else:
        return values[math.ceil((len_of_values - 1) / 2)]
