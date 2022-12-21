var = {111, 22, 53, 4, 4, 3}
print("set sample is ", var)
# we can see in the output that the order is random, hence sets are unordered unlike lists or tuple


# Accessing set items
# using for loop

for i in var:
    print(i)

# add or remove items to/from set

# to add single item in the set
var.add(10)
print(var)

# to add more than one item to the set, create any iterable and then use update method to add
car = {'merc', 'bmw'}
var.update(car)
print(var)

# remove items from set
var.remove('merc')
print(var)

var.remove('bmw')
print(var)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set,
# then remove() raises an error, whereas discard() does not raise any error.

# to remove elements from the set we do have below methods as well:
# pop() -> challenge here is, since it is unordered we dont know which item will be popped, can assign the popped
#           value to a variable
# del() -> deletes the set entirely
# clear() -> clears the content of the set


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
