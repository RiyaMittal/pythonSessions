# to create new list on the fly using other iterables like list/tuple/dict/sets/arrays of range etc

lst1 = [1,2,3,4]
lst2 = [x**2 for x in lst1]
print(lst2)


lst33 = [x for x in lst1 if x%2==0]
print(lst33)
#

# lst = []
# for i in lst1:
#     lst.append(i**2)
# print(lst)

lst3 = [i for i in range(4)]
print(lst3)
#
# for i in range(10):
#     print(i)