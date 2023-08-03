# Python Numbers
# Numeric data types in Python = int, float & complex

x = 1 # int
y = 11.5 #float
z = 3j #complex

# Type Conversion

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#N.B: You can't convert complex to another

# Random Number
# Using random() function
# import first though
import random

print(random.randrange(1,10))