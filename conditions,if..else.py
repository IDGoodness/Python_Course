# Python supports the usual logical conditions from mathematics:

#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b

# We can use conditional statements in python code for different reasons. 
# We use the if keyword.
# A colon is used.
# Indentation is important!

a = 33
b = 200
if b > a:
  print(f"{b} is greater than {a}")
  
# To have more than one conditions, the Elif statement is used.

a = 33
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")
  
# To print an alternative condition, we use the else statatement.

a = 200
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")
else:
  print(f"{a} is greater than {b}")
  
# Shorthand, you put the statement in front of the condition.

# Shorthand if..else
a = 2
b = 330
print("A") if a > b else print("B")
# You can also use or keyword for the above

# Nested if, and if statement inside another
# pass statement, for empty statements.