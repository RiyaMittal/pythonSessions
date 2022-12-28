"""
To perform any task on a file, we first need to open it using open() function.
This function will give a file object with read() method to read the contents of the file

"""

file = open("sample.txt")
print(file.read())

"""
Modes of reading a file:
read(r): this mode is for read only purpose, if file does not exist then we get error. DEFAULT MODE
write(w): it opens the file in write mode, if file does not exist then it creates the file.
append(a): it opens the file in append mode and creates the new file if the file does not exist.
create(x): this mode creates the file and gives error if file does not exist.

Apart from these modes we also need to specify how the file must be handled:

text (t): Used to handle text files.
binary (b): used to handle binary files (images).
"""

x = open("sample1.txt",'w')
x1 = open("sample2.txt",'a')
x2 = open("sample3.txt",'x')

