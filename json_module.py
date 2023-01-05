"""
easy to parse

"""

import json

# loads
# load

# json should have double quotes ("")
# string to json
data = '{"var1":"harry", "var2":56}'  # parse this data

parse = json.loads(data)
print(parse)
print(type(parse))
# print(data)
# this output looks same as above , but you can not use parse['var1'] here. u can not parse the data
# since it is a string

# task1 -> read about json.load

# json.dumps

data2 = {
    "channel_name": "zeetv",
    "cars": ['maruti', 'bmw', 'audi', 'ferrari'],
    "fridge": ('roti', 'dosa')
}

# dictionary to json right now data2 will give error as JSON object, it will work in python but not in javascrpt,
# so to make it java script compatible:

print(json.dumps(data2)) # now u can use in java script


# task2 -> what is sort_keys , indent parameter in dumps