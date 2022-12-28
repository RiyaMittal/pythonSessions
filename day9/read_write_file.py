"""
Reading from a file and writing to a file
"""

# create a file

file = open("myfile.txt",'x')
file.close()
#write onto a file

file = open("text.txt",'w')
file.write("this is an example of file creation")
file.close()

# if file is already there, then write method will overwrite it

file= open("text.txt",'w')
file.write("overwriting the content...")
file.close()

# #read a file
# file = open("sample.txt",'r')
# print(file.read())
# file.close()
#
#
# #append a file
file = open("sample.txt",'a')
file.write("appending the data")
file.close()
