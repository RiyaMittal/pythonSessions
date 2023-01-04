# we used format on strings to use variables in them. but in latest versions, we can use fstrings. which
# you may find better

str = "My name is {} and I live in {}"
name = "Python"
city = "Delhi"

final_str = str.format(name, city)
print(final_str)

# now i can use fstrings also to the above

print(f"My name is {name} and  I live in {city}")

# we can also print only variable names using double braces

print(f"My name is {{name}} and I live in {{city}}")