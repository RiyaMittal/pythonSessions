# calling a function by itself is called recursion

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:

        return num * (factorial(num - 1))


# Driver code
num = 7
print("number", num)
print("factorial of {} is {}".format(num, factorial(num)))
