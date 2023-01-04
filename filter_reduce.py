"""
filter- tests a specific user defined condition for a function and returns an iterable of elements that satisfy the condition
syntax: filter(function , iterable)

"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    if num > 5:
        return num


gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)

"""
reduce - it applies a function to every item of an iterable and gives back a single value as a result
"""

from functools import reduce

lst1 = [1, 2, 3]
a = reduce(lambda a, b: a * b, lst1)
print("output of reduce", a)
