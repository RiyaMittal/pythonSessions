colors = {"RED":"Roses","Blue":"Sky","Pink":"Flower"}
# to access dictionary

print(colors['RED'])
print(colors.get('Blue'))

# to access multiple values:

print(colors.values())
print(type(colors.values()))

# access keys in dict

print(colors.keys())

#access key value pair

print(colors.items())

for i in colors.items():
    print(i)