# how to check if items of one set are present in other set?
# methods to check that are:
# isdisjoint()
# issupperset()
# issubset()

nums = {1, 2, 3, 4}
numb = {9, 7, 5, 2, 3}

print(nums.isdisjoint(numb))  # returns FALSE if items are present else True
print(nums.issuperset(numb))  # checks if all the items of a particular set are present
# in the original set.

print(nums.issubset(numb))  # if all the items of the original set are present in the particular set.
# returns FALSE is items are present else True
