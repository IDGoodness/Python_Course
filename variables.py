# Python Variables

# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 2
Y = "John"
z = 3
print(x)
# print(y)
print(Y)
print(z)
print(x * z)

# Variables do not have a fixed data type, the data type can be changed

x = 2 #x is an integer here
x = "Sally"  # x changed, it is now a string

# Variable names and naming

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Assigning values to multiple varibles

x, y, z = 2, 3, 4
print(x * y)

# Output Variables, print() statement is used

x = "awesome"
print("Goodness is " +x)
print(f"Goodness is {x}")
print("Goodness is " +x+ " and smart!")
print(f"Goodness is {x} and smart!")

y = "Python"
z = " is "
c = "awesome"
print(y + z + c)


# Global Varibles

x = "smart"

def myfunc():
    print(f"Goondess is {x}")
    
myfunc()

# global keyword is used to make a variable global anywhere

def myfunc1():
    global y
    y = 2

myfunc1()
print(y)