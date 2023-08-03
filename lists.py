# Python Lists
# Meaning
# List is a collection which is ordered 
# and changeable. 
# Allows duplicate members.
# Written in square brackets

myList = ["apple", "mango", "cashew"]
print(myList)
print(type(myList))

# Accessing items in the list i.e. Indexing
# print the second item in the above list
print(myList[1])

# use negative indexing to print the above
print(myList[-2])

# Range of indexes
# It will be a new list
myList2 = ["apple", "mango", "cashew", "cherry", "orange", "watermelon", "coconut"]
print(myList2[2:5])
# N.B: leaving out the start auto starts at 1st list
# N.B: leaving out the end auto ends at the last list

# This is same for negative indexes too.

# Changing Item Value
# To change the value of a specific item in a list, do it by refering to its index.
# Using myList
# Change mango to carrot
myList[1] = "carrot"
print(myList)

# Looping through a list 
# Using a for loop
# Loop (i.e. print all values one by one) through myList2.
for i in myList2:
    print(i)
    

# Checking if an item exists
# We use the in keyword
# Check if we have "orange" in myList2
if "orange" in myList2:
    print("You have an orange in your bag!")
    

# List Length
# Finding the number of items in a list
# Use the len() function.
# Find the length of myList and myList2
print(len(myList))
print(len(myList2))


# Adding items to a list
# Use the append() and insert() functions
# append() to add at end
# insert() to add at specified location, takes argument
myList3 = ["apple", "mango", "cashew", "cherry"]
# add carrot to the list
myList3.append("carrot")
print(myList3)

# add orange just after mango
myList3.insert(2, "orange")
print(myList3)


# Removing items from a list
# Use the remove() and pop() functions
# remove() removes specified item
# pop() removes specified index, or last item if index not provided.
# del() specified index
# clear(), clears the list

myList4 = ["apple", "mango", "cashew", "cherry", "orange", "watermelon", "coconut"]
# I'll remove watermelon from the list using both methods. PS, I don't like watermelon!
myList4.remove("watermelon")
print(myList4)

myList5 = ["apple", "mango", "cashew", "cherry", "orange", "watermelon", "coconut"]
myList5.pop(-2)
print(myList5)


myList6 = ["apple", "mango", "cashew", "cherry", "orange", "watermelon", "coconut"]
del myList6[-2]
print(myList6)

# del() can also clear list
del myList6


# Let's clear myList6
myList5.clear()
print(myList5)


# Copying a list
# Use the copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Using the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Joining two lists
# Use the + operator
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Using the append() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

# for x in list2:
#   # list1.append(x)

# print(list1)