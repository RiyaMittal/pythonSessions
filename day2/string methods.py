sample = "  riya Mittal is taking python classes !!!"

print(sample.upper())  # it will convert all characters of string into uppercase
print(sample.lower())  # it will convert all characters of string into lowercase

print(sample.strip())  # it will strip all the white spaces before or after the string

sample2 = "hello !!!"  # only the trailing character . even if i gave ! here to strip but if
# there is a space at the end then it will strip that because it is trailing
print(sample.replace("!","?"))  # it replaces the string with another string
print(sample.replace("riya","abcs"))

ss = "Monday,Tuesday,Wednesday"
print(ss.split(","))  # it splits the string by the delimiter given and then returns the list of those elements
print(sample.capitalize() ) # here the first character is space so no effect can be seen
# it capitalizes only the first character of teh string. and all other characters in small case

sample3 = "riyA Mittal"
print(sample3.capitalize())

print(sample.center(50))  #This method aligns the string to the center as per the parameters given by the user.
print(sample.center(50,"+"))  #This method aligns the string to the center as per the parameters given by the user.

sample4 = "abracadabra"
print(sample4.count('a')) # it counts the frequency of a given value in the string
print(sample4.endswith('a')) # it returns True if it endswith a given value else False

print(sample4.startswith('a')) # it returns True if it starts with a given value else False

print(sample.find("riya")) # searches for the first occurrence of the given value and returns the index where it is
# present. If given value is absent from the string then return -1.
print(sample.find("Jothi")) # wil return -1

print(sample.index("riya")) # searches for the first occurrence of the given value and returns the index where it is
# present. If given value is absent from the string then raise an exception.
# print(sample.index("Jothi"))

print(sample.isalnum())  #returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters
# or punctuations are present, then it returns False.

print(sample.isalpha())  #returns True only if the entire string only consists of A-Z, a-z. If any other characters
# or punctuations or numbers(0-9) are present, then it returns False.

print(sample.islower())  #returns True if all the characters in the string are lower case, else it returns False.
print(sample.isupper())  #returns True if all the characters in the string are upper case, else it returns False.

sample5 = "Hello,\t \t.Mike"
print(sample5.isprintable())

sample6 = "        "       #using Spacebar
print(sample6.isspace())  # if all characters are space then True else False
sample7 = "        "       #using Tab
print(sample7.isspace())
print(sample.isspace())

print(sample.istitle())  # True if first letter of each word is in caps else False
sample9 = "Riya Mittal Jothi"
print(sample9.istitle())

print(sample.swapcase())  # changes the character casing of the string
print(sample.title())  # capitalizes each character of the word