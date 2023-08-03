# Python does not have built-in support for arrays, but list is used.
# List processes can be done here.

# Arrays is used to store multiple values in a single variable.

car = ["Tesla", "BMW", "Toyota"]


# Accessing elements in an array
# Get the value of the first element in the array above.

print(car[0])

# Modify the value of the first item
car[0] = "Honda"
print(car)

# Length of an array
# use len()

print(len(car))

# Looping through array

for i in car:
    print(i)

# Adding elements
car.append("Tesla")
print(car)

car.append("Volvo")
print(car)

# Removing elements
car.pop(0)
print(car)
car.append("Volvo")
print(car)
car.remove("Volvo") #N.B list remove only removes the first occurrence of the specified value element
print(car)