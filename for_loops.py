# For loops is used to "loop", go through either a list, tuple, dictionary etc.
fruits = ["apple", "banana", "mango"]
for x in fruits:
  print(x)
  
# Looping through a string.
for y in "Goodness":
    print(y)
    
# Break statement: just like break in while loop
fruits = ["apple", "banana", "mango"]
for z in fruits:
  print(z)
  if z == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "mango"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
# Continue Statement: just like in while loop
fruits = ["apple", "banana", "mango"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# The range() function
# To loop through a set of code a specified number of time
for x in range(6):
  print(x)

for x in range(2, 6): #prints the values, starts from 2
  print(x)

for x in range(2, 30, 4): #steps by 4, default is one
  print(x)
  
  
# Else in loop;
# Specifies block of code to be executed after the loop
for x in range(11):
  print(x)
else:
  print("I looped from 1 to 10!")
  

# Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "mango"]

for x in adj:
  for y in fruits:
    print(x, y) 
    
# The pass statement, put when loop is empty
for x in range(6):
  pass