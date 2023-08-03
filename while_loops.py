# Python Loops
# While Loops
# For Loops

# Executing a set of command while a condition is True
i = 1 # While loops require a variable to be ready.
while i < 6:
    print(i)
    i += 1 # This adds 1 to i after the condition is fulfilled. Or infinite loop starts
    
# Break Stattement: You can stop the loop, even if the condition is true.
# Exit the loop when i is 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# Cotinue Statement: Stop with the current iteration and continue with the next.
# Continue to the next iteration if i is 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# Else statament: With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  

# Exercise, print i as long as i is less than 10