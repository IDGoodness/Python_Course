# A block of code that runs only when called
# def keyword is used to create a function

def my_func1():
    print("Hello, World, function!")
    
my_func1() # I called the function here.

# Arguments, info can be passed into functions as arguments

def my_func2(name):
    print(name + " Goodness")
    
my_func2("Adewuyi")

# correct number of arguments
def my_func3(fname, lname, mname):
    print(f"{fname}, {lname} {mname}")
    
my_func3("Goodness", "Adewuyi", "Adeyinka")

# we use * when we don't know number of args passed

def my_function(*kids):
  print("The youngest child is " + kids[2])
  print(f"The youngest child is {kids[2]}")

my_function("Emil", "Tobias", "Linus")

# keyword argument

def my_func4(child1, child2, child3):
    print(f"The youngest child is {child3}")
    for x in child2:
        print(x)
    
my_func4(child3="Sola", child1="Ade", child2="Bola")

# arbitrary keyword argument
# Not knowing how many keyword argument passed

def my_func5(**kid):
    print("His last name is " + kid["lname"])
    
my_func5(fname = "Ade", mname = "Olu", lname = "Chike")


# Default parameter value.
# Used when args is not passed

def my_func6(country = "Nigeria"):
    print(f"I am from {country}")

my_func6()
my_func6("South Korea")
my_func6("Canada")

# Passing a list as a statement

def my_func7(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "carrot"]

my_func7(fruits)

# Return values

def my_func8(x):
    return 5 * x

print(my_func8(3))
print(my_func8(10))
print(my_func8(5))

# The pass statement: when the function can't be empty
def my_func9(name):
    pass
