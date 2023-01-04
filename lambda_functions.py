def sum(a,b):
    return a+b

sum_lambda = lambda x,y:x+y

print("sum",sum_lambda(1,2))



result = lambda x,y,z: x+y+z

print("sum of all 3 values", result(1,2,3))


