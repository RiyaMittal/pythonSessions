"""
we have 4 types of arguments in function definition in python functions
1.default
2.keyword
3.required
4.variable length
Let's see DEFAULT ARGUMENTS:
"""


def full_name(salutation, first="RIYA", last="MITTAL"):
    print("Hi", salutation, first, last)


full_name("Mrs")

