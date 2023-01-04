#os stands for operating system
"""
renaming a file
new folder creation
see the contents of a directory
etc...
"""

import os

# print(dir(os))

#current working directory
print(os.getcwd())
# change the current working dir
# os.chdir("/Users/")
# print(os.getcwd())
# f = open("enumerate.py") # cwd is changed now

#list dir
print(os.listdir())
print(os.listdir("/Users/"))

# os.mkdir("This")
# os.mkdir("This/that")# not working is This is not there
# os.makedirs("This/that")

# os.rename("riya.txt", "riya11.txt")

#to read env variables

print(os.environ.get("HOME"))

print(os.path.join("/Users","riya.txt")) #joins two paths

print(os.path.exists("/Users/"))# tells if the path exists or not

print(os.path.isfile("/Users/riya.txt"))

#similarly we have many other methods in this module.