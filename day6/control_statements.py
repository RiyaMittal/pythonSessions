# pass
"""
An empty code inside loop, if statement or function will give an error.
To avoid such an error and to continue the code execution, pass statement is used.
pass statement acts as a placeholder for future code.
"""

for i in range(6):
    pass

# continue
"""
This keyword is used in loops to end the current iteration and continue 
the next iteration of the loop. Sometimes within a loop, we might need to skip a specific iteration. 
This can be done using the continue keyword.
"""

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)



# break
"""
The break keyword is used to bring the interpreter out of the loop and into the main body of the program. 
Whenever the break keyword is used, the loop is terminated and the interpreter starts executing 
the next series of statements within the main program.
"""
i = 1
while i <= 10:
    i = i + 1
    if i == 5:
        break
    print(i)
