"""
syntax:
enumerate(iterable, start=0)
"""


lst = ["orange", "apple", "strawberry", "banana"]
# I want to print all fruits at even indices in the list

for i in range(len(lst)):
    if i %2 == 0 :
        print(lst[i])

print()
#instead of using this, I can index the list using enumerate function

for index,item in enumerate(lst):
    if index%2==0:
        print(item)


print(list(enumerate(lst)))

