# accessing list items using index

list1 = [1, 4, 11, 9]
print(list1[1])
print(list1[3])

# Positive indexing
print("above example shows how to access list elements using positive index")

# negative indexing- last element can be accessed using -1 in lists
# and then to move backwards same sequence is followed. -1,-2,-3

print("last element in the list", list1[-1])
print("last element in the list", list1[len(list1) - 1])  # better to remember it this way for negative indexing

# printing elements in a range

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]

print(animals[3:8])
print(animals[3:-3])

# jump index
print(animals[2:7:2])
print(animals[::2])  # using positive index
print(animals[-8:-1:2])  # using negative index

print(animals[:])  # by default first is 0 and last is len(list)
print(animals[:-1])  # default first is 0
print(animals[0:])  # till end
print(animals[:len(animals)])  # till end


