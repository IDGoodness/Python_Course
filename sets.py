# Sets is a collection which is unordered and unindexed.
# Sets is written with curly {} brackets.

my_set = {"apple", "mango", "carrot"}
print(type(my_set))

# Set Operations
# You cannot access items in a set because it is unordered.

# Loop through a Set
my_set = {"apple", "mango", "cashew", "carrot"}

for x in my_set:
  print(x)

# Checking items in a Set
print("mango" in my_set)


# You cannot change the items in a set

# You ca add to a set using .add()
my_set.add("banana")
print(my_set) # adds banana from the front


# You add multiple(a list) items to a set, using 
# .update()
my_set.update(["orange", "grapes", "coconut"])
print(my_set) # starts adding from the last


# You can do other processes like get length, remove item(you can use the list methods)


# Join two sets
# union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)