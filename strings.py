# String Literals

# With '' or "" 

a = "Hello, World!"
print(a)

    # Multi Line String

b = """
Muirvnri birv
vruyieu eib ebuvr
reubvr
ebvriuvri
"""
print(b)

# String Slicing, indexing

c = "John Doe"
print(c[2:5]) #Starting from position 2 and stops at 5, without the 5th.


# Negative Indexing, Slicing

d = "John Doe"
print(d[-5:-2])

# String Length, len()

e = "John Doe"
print(len(e))


# .strip() removes whitespace from beginnig or end
f = " Hello, World! "
print(a.strip())

# .lower() & .upper, changes the case, lower & upper

g = "Hello, World!"
print(g.lower())
print(g.upper())

# .replace(), takes argument, replaces a string with another.
h = "Gello, World!"
print(h.replace("G", "H"))


# .split() takes argument(separator),
# splits the strings if it finds 
# instances of the separator

i = "Hello, World!"
print(i.split(","))

# Check String
# Check if "ain" is present

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if "ain" is NOT present

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation
# merge variable a and b into c

a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format
# Combine str and int is possible with format()
# format() & {}

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# passing arguments into format()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# passing arguments, using indexing
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# Escape Character, using quotes in quotes
txt = "We are the so-called \"Vikings\" from the north."
print(txt)