# Do not use reserved
'''
print('Hello World')

print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = 10 # shortcut for below.  works but not recommended

print (a,b,c)


# Statement vs Expression

x = 47  # statement
y = x + 10  # expression


# TYPE CONVERSION --> to change the data type of a variable
# Convert floats and numeric strings to int
print(int('20'))
print(type(int('20')))
# print(int('20.24'))  # errors out because int expects only whole numbers inside quotes
print(float('20.24'))
print(type(float('20.24')))


## STRINGS ##
# 3 Ways to create a string - using either single, double, tripe quotes
first_name = 'Jane'
last_name = "Doe"
address = "10 Main St."

job = "Physician's Assistant"  # recommended to use double quotes for strings

## String Functions
# len() → returns the number of characters in a string
print(len("Hello"))

# upper and lower → conver the string to appropriate case
print("hello".upper())

# String concatenation - adding up strings
first_name = "Jane "
last_name = "Doe "
print(first_name + " " + last_name)
age = 24
print(first_name + last_name + ":" + " " + str(age))

#String multiplication - can multiply a string with an int
print("hello"*3)
'''

# Accessing string characters - a string is just a sequence of characters
name = "Jane Doe"
print(name[2])  # equals n
# print(name[8])  # throws out of bounds error

# Retrieving the character at a given index
print(name.index('o'))  # equals 6
print(name.index('e'))  # returns the index of first occurence






