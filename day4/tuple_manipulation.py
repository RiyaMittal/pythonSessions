countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# unpacking of tuple
(a,b,c) = countries[:3]
print(a)
print(b)
print(c)

# But what if we have more number of items then the variables?
# You can add an * to one of the variables and depending upon the position of variable and number of items, python
# matches variables to values and assigns it to the variables.

(*a,b,c)=countries
print(a)
print(b)
print(c)

(a,b,*c) = countries
print(a)
print(b)
print(c)