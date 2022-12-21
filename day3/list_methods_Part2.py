#removing items from the list

#pop() - it removes last item from teh list if no index given, else removes
# the item of the index specified

days = ["Mon","Tue","Wed","Thur","Fri","Sat"]
days.pop()
print(days)

days.pop(-1)
print(days)

# remove() - it removes a specific item from the list

days.remove("Mon")
print(days)

# del - it deletes the item from a specific index or entire list also

del days[1]
print(days)
#
# del days
# print(days)

# to delete all items in the list not the list itself- empties the list
days.clear()
print(days)

