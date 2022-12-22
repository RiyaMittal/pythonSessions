# adding items to dict

#we can create a new key and then assign the value to it

movies = {"tamasha":"hindi","conjuring":"english","drishyam":"malyali","sitaramam":"telugu"}
movies['honsla rakh'] = "punjabi"

print(movies)

# using update method

movies.update({"drishyam":"hindi","avatar":"english"})
print(movies)

# removing items from a dict

movies.clear() # clears all items from the dict
print(movies)

movies = {"tamasha":"hindi","conjuring":"english","drishyam":"malyali","sitaramam":"telugu"}
movies.pop('tamasha') # pops the key value pair whose key is passed in pop
print(movies)

movies.popitem()  # pops the last keyvalue pair
print(movies)

del movies['conjuring']
print(movies)


# copy dictionary

newdict = movies.copy()
print(newdict)

new_dict = dict(movies)
print(new_dict)