def add(a, b):
    return a + b


def minus(a, b):
    return a - b


# x = minus(2,1)
# print("in file 1 minus", x)
#
# y = add(10, 20)
# print("in file 1 add", y)

# if __name__ == '__main__':
#
# __name__ = '__main__'
# __name__ = script_name



print('value of name variable is ', __name__)
if __name__ == '__main__':
    x = minus(2, 1)
    print(x)

    y = add(10, 20)
    print(y)
    z = x+y
