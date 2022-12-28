# try except block in python is used to handle errors and exceptions

try:
    num = int(input("Enter an integer: "))
except:
    print("Number entered is not an integer.")

# try:
#     num = int(input("Enter an integer: "))
# except ValueError as e:
#     print("Number entered is not an integer.",e)


"""
In addition to try and except blocks, we also have else and finally blocks.

The code in else block is executed when there is no error in try block.

The finally block is execute whatever is the outcome of try……except…..else blocks.

"""

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
