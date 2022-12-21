# how to join two separate strings??

a = "Riya"
b = "Mittal"

print(a + ' ' + b)

# if one is number and other is string?

c = 10

# print(a+ ' ' + c)

# we use format() method to achieve this

print("first string is {} and second number is {}".format(a,c))

# also can use indexing for this to place the args in a specified format

print("first string is {0} and second number is {1}".format(a,c))

quantity = 2
fruit = "Apples"
cost = 120.0
statement = "I want to \t buy  {2} dozen {0} for {1}$"
print(statement.format(fruit,cost,quantity))


