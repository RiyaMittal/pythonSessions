# to add an item to the existing list

lst1 = [2, 12, 100, 19, 1]
lst1.append(1000)
print(lst1)

#insert an item in the middle of the list at a particular index
lst1.insert(2,555)
print(lst1)

# to append an entire list/tuple/dict/set to the existing list
lst2 = [111,222,333]
# tup = (11111,22222)
# dit = {"a":1,"b":2}  # for dictionary it adds only the keys not the values
lst1.extend(lst2)
print(lst1)

# concatenating two lists

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)