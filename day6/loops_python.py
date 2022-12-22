"""
for loops can iterate over a sequence of iterable objects in python.
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
"""

colors = ("Red", "Green", "Blue", "Yellow")
for x in colors:
    print(x)

for k in range(5):
    print(k)

"""
As the name suggests, while loops execute statements while the condition is True.
 As soon as the condition becomes False, the interpreter comes out of the while loop. 
"""

count = 5
while (count > 0):
    print(count)
    count = count - 1

# we can use else in while also

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

#nested loops

for i in range(1, 4):
    k = 1
    while (k<=3):
        print(i, "*", k, "=", (i*k))
        k = k + 1
    print()