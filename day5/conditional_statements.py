# if-else

age = 10

if age >= 18:
    print("Can vote")
else:
    print("can not vote")


# if you have more than one condition to evaluate then we can use elif statment with if-else

num = 0
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is ZERO")

# nested if-else statements

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")