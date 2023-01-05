"""
iterable - they have functions like __iter__() and __getitem()__, when we call __iter__() on them then we get an iterator
iterator - they have functions like __next__().

for eg. list, if we can run in forloop to get all element - then it is iterable  and then it gives iterator

iteration -> the process of iterating over an iterable is called iteration
generators - > they are a type of iterator, can only traverse once

"""

# for i in range(78):  # generating on the fly, may be we dnt have ram for this to be stored
#     print(i)


# range -> generator, once done, we cant go back

# yield keyword return -> return value of a function. nthing runs after that print -> prints on console and function
# continues yield -> on the fly generates -> it gives generator object, why? to save ram -> it is capable of
# generating this many numbers , when needed i can generate ( like sone ka ande wali murgi, when needed i will take)

# def gen(n):
#     for i in range(n):
#         yield i


# g = gen(12345678)
# print(g)

# g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# same is there in for loop ->
#
# for i in g:
#     print(i)

# not getting StopIteration because for loop handles that error automatically

# h = "harry"  # iterable ( you can iterate)
# # print(iter(h)) -> give string iterator and then run __next__() method on that
# itr = iter(h)
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__()) # so on and so forth

# for char in h:
#     print(c)


# fibonacci series till n number
# factorial

