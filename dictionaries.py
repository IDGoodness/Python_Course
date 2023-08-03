# Python Dictionary
# It is unordered, but changeable and it's indexed like a list.

my_dict = {
    "name" : "Mike",
    "age" : "16",
    "car" : "Tesla",
    "year" : "2023"
}
print(my_dict)
print(type(my_dict))


# Accessing items in a dictionary
# Get the name of the person in the dictionary above
print(my_dict["name"])
# You can do stuffs like this to get things in the dictionary
# What we use in accessing these "values" is called the "key"
# The "key" is uesd to access the "value"

# Getting value of a key
# 1. Default Method
x = my_dict["car"]
print(x)

#2. Using get() method
y = my_dict.get("year")
print(y)


# Changing the value
# You can do this by refferring to the key.

# Change the car year to 2023
this_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["year"] = 2023
print(this_dict)

# Loop through a dictionary

a_dict = {
    "name": "Goodness",
    "age": 87,
    "nick": "Chrestotes",
    "DOB": 1936,
}

# Looping through the dictionary above
for i in a_dict:
    print(i)
    # This only loops through the key
    
for i in a_dict:
    print(a_dict[i])
    
    
# To return values, we use the values() function
for i in a_dict.values():
    print(i)
    
# We can loop through all keys and values. items()
for i, j in a_dict.items():
    print(i, j)
    
# To check if key exists
# Check if DOB exists in a_dict
if "DOB" in a_dict:
    print(True)
    
# Check length
print(len(a_dict))

# Add car and Tesla to a_dict.
a_dict["car"] = "Tesla"
print(a_dict)

# To remove, pop()
# Remove DOB from a_dict
a_dict.pop("DOB")
print(a_dict)

# popitem(), removes last item entered
# In this case, it removes car and Tesla
a_dict.popitem()
print(a_dict)

#Some other operations can be done....