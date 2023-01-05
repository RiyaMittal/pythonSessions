"""

"""


# def function1():
#     print("like this course")
#
#
# func2 = function1  # assigning one function to other
# # del function1
# func2()

# function inside a function


# def funcret(num):
#     if num==0:
#         return print # returning function
#     if num ==1:
#         return int  # returning function
#
#
# a = funcret(0)
# print(a)

# so it means we can return a function using a function
# also we can pass func as an argument ->


# def executor(func):
#     func("this is called from a function argument")
#
# executor(print)


# +++++++++++++++++++decorator++++++++++++++++++


def decfunc(func):
    def execunow():
        print("executing it now")
        func()
        print("executed already")

    return execunow


# @decfunc
def planet_name():
    print("We live on Earth planet ")


# planet_name = decfunc(planet_name)
planet_name()


# if we have to do same task for multiple functions, then we can make a function as a decorator and apply it on all