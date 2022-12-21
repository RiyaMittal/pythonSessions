# It allows us to insert illegal characters into a string like a back slash,
# new line or a tab.
#Single/Double Quote: used to insert single/double quotes in the string.
# "riya mittal \"jothi\""

str1 = "He was \"Flabergasted\"."
str2 = 'He was \'Flabergasted\'.'
print(str1)
print(str2)


# new line character to insert a new line wherever needed
str1 = "I love doing Yoga. \nIt cleanses my mind and my body."
print(str1)

# tab to insert a tab \t
str2 = "Hello \t\tWorld \t!!!"
print(str2)

# Backspace: erases the character before it wherever it is specified.
str2 = "Hello\bWorld !!!"
print(str2)

#Backslash: used to insert a backslash into a string.

str3 = "What will you eat? Apple\Banana"
print(str3)