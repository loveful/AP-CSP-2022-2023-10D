'''
Comments are green and used to explain code, they start with #
Python has no object for declaring the datatype, a variable is created the moment you first assign a value to it.

x = 5
y = "John"

print(x)
print(y)

# Variables have types
x = 4 # x is of type int
x = "Sally" # x is of type string

# Casting
# Casting is to specify the datatype of a variable
x = str(3) # 3 will be a string assigned to x
y = int(3) # 3 will be a integer assigned to y
z = float(3) # 3 will be a float (3.0) assigned to z

# How to print the type
x = 5
y = "John"
print(type(x)) # Prints the type of x
print(type(y)) # Prints the type of y
# Note: " is same '' so "x" is same as 'x'
# Case Sensitivity
a = 4
A = "Sally"
# A will NOT overwrite a

# Naming Variables
# 1. A variable name must start with a letter or a _
# 2. A variable name cannot start with a number
# 3. A variable bane are case sensitive

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Namings

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(f"{x}\n{y}\n{z}")

# Assign 1 value to multiple variables
x = y = z = "Orange"
print(f"{x}\n{y}\n{z}\n")
'''

# Random Number
import random

print(random.randrange(1, 10))

# Concatentation
a = "Hello"
b = "Patricia"
c = a+" "+b
print(c)

# String Format
age = str(36)
txt = "My name is Patricia, I am "+age
print(txt)


# Escape Characters
# To insert characters that are illegal in a string, use a escape character, in this case \
#text = "We're fabulous" Unicorns "from amazingland"
text = "We're fabulous \"Unicorns\" from amazingland"
print(text)
