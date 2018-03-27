"""
### This is a very simple program that illustrates the difference between raw_input and input
    -- Encountered in a Hackerrank problem and took few minutes to figure out

### We already know of the vulnerability that takes in a raw_input which takes an input and also matches with any possible variable name inside python.

### Even then the difference is not spotted so I wanted to make a note here. The input function, takes an input only as the given datatype, you gotta explicity use "" for a string. But for raw_input this is not the case, it would accept any ascii value 
"""
z = input()
print z
y = raw_input()
print y


# Declare second integer, double, and String variables.
x=0
y=0.0
z=""
# Read and save an integer, double, and String to your variables.
x = input()
y = input()
z = raw_input()
# Print the sum of both integer variables on a new line.
print(x+i)
# Print the sum of the double variables on a new line.
print(y+d)
# Concatenate and print the String variables on a new line
print(s+z)
# The 's' variable above should be printed first.

