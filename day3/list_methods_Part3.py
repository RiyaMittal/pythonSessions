#sort- in ascending order

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

num.sort(reverse = True)
print(num)

# reverse: reverses the order of the list
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# index: returns index of the first occurence of the item
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.index(2))

#count = count the frequency of an element in the list
print(num.count(2))

# copy

animals1 = animals # not recommended . its not a copy its just a reference.
animals1[0] = "Elephant"
print(animals)

# to create a copy, use copy()
animals2 = animals.copy()
animals2[0] = "Lion"
print(animals)