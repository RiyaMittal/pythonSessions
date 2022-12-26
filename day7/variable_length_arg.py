"""
Variable-length Arguments
1. While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of tuple.
"""


def full_name(*name):
    print("Hi,", name[0], name[1])


full_name("RIYA", "MITTAL")
full_name("JOTHI", "RAJKUMAR")

"""
2.While creating a function, pass a ** before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of dictionary.
"""


def full_name(**name):
    print("hi,", name['first'], name['last'])


full_name(first="RIYA", last="MITTAL")