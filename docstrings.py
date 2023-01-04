"""
docstrings are used to maintain input output param type details for any class, methods, functions
they are written just after the defintion declaration
we can access the docstring using the attribute __doc__
"""

def print_int(a):
    """

    :param a: input of type integer
    :return: print statement
    """

    print("value of a is ", a)

print_int(2)
print(print_int.__doc__)


def abc():
    a = 2
    """
    is this docstring or comment??
    """

    return f"value of a is {a}"

print(abc())
print(abc.__doc__) # comments are not recognized by interpreter