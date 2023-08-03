# Python Operators
    # Arithmetic operators
    # Assignment operators
    # Comparison operators
    # Logical operators
    # Identity operators
    # Membership operators
    # Bitwise operators


# Arithmetic Operators
# (+, -, *, /, %, **, //)

# global x
# global y

x = 6
y = 3
# Addition (+)
print(x + y)

# Subtraction (-)
print(x - y)

# etc, *, /, %, **, //
# % gives us the remainder in a division
#the floor division // 
# rounds the result down to the nearest whole number


# Assignment Operators
# (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)

x = 5
x += 2 # same as writing x = x + 2
print(x)


# Comparsion Operator
# ==, !=, >, <, >=, <=
x = 2
y = 5

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
    
# Logical Operators
# and, or, not
# and: Returns True if both statements are true
x = 5

print(x > 3 and x < 10)
# returns True because 5 is greater 
# than 3 AND 5 is less than 10

# or: Returns True if one of the statements is true
x = 5

print(x > 3 or x < 4)
# returns True because one of the 
# conditions are true (5 is greater than 3, 
# but 5 is not less than 4)

# not: Reverse the result, returns False if the result is true
x = 5

print(x > 3 and x < 10)
# returns False because not is 
# used to reverse the result


# Identity Operators
# is, is not
# is: Returns true if both variables are the 
# same object
x = 2
y = 3
print(x is y)

# is not: Returns true if both variables are not
# the same object
print(x is not y)
