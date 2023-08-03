my_tuple = ("apple", "banana", "cherry")
print(my_tuple)


# Indexing
# Print out "banana" from the list with -ve and +ve indexing
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])
print(my_tuple[-2])


# Range, +ve and -ve
# Range of +ve index
my_tuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# Print the fruits from start to end
print(my_tuple2[:]) # method 1
print(my_tuple2[0:]) # method 2
print(my_tuple2[0:7]) # method 3

# Range -ve index
# Print the fruits from start to end
print(my_tuple2[-7:])

# You can do more with tuples
# Except that it is immutable;
# You can loop, check if item exist, find its length and join two tuples.