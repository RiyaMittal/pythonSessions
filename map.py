"""
map function: it executes certain instructions or funcitonality to every item of the iterable
syntax: map(function, iterable)
"""

numbers = ['1', '2', '3', '4']
# without map

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print("without map", numbers)

result = list(map(int, numbers))

print("with map", result)

num = [1, 4, 8, 10, 12, 15]
sq_num = list(map(lambda x: x * x, num))
print("square of list items", sq_num)


#####
# if we have 2 functions and we want to apply both on items of a list simultaneously

def sq(num):
    return num * num


def cube(num):
    return num * num * num

# cube = lambda x:x*x*x


lst_func = [sq, cube]
for i in range(10):
    result = list(map(lambda x: x(i), lst_func))
    print(result)

# sq(0),cube(0)
# sq(1),cube(1)
# sq(2),cube(2)