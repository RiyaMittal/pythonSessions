# like mathematics, we can perform union, intersection on sets in python as well

#union() -> gives new set by union of two sets ( all items)
# update() -> updates an existing set by adding the other set to it

city1 = {'Delhi','Mumbai'}
city2 = {'Chennai','Kolkata'}

metro_cities = city2.union(city1)
print(metro_cities)

ncr_cities = {'Delhi','Ghaziabad','Noida'}
city4 = {'Gurugram'}
ncr_cities.update(city4)
print(ncr_cities)

#intersection() - > gives items similar in both sets - returns new set
#intersection_update() -> update the existing set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#symmetric_difference -> prints items not similar to both sets - new set in result
#symmetric_difference_update-> update the existing set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#difference() ->returns items present in original set not in both the sets - new set in result
#difference_update()-> update existing

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)
