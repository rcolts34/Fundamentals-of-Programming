####### Adding a comment in remote repo
# Do not use reserved
'''
print('Hello World')

print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = ( ) # shortcut for below.  works but not recommended

print (a,b,c)


# Statement vs Expression

x = 47  # statement
y = x + 2  # expression


# TYPE CONVERSION --> to change the data type of a variable
# Convert floats and numeric strings to int
print(int('20'))
print(type(int('20')))
# print(int('20.24'))  # errors out because int expects only whole numbers inside quotes
print(float('20.24'))
print(type(float('20.24')))


## STRINGS ##
#  Ways to create a string - using either single, double, tripe quotes
first_name = 'Jane'
last_name = "Doe"
address = "02.19.24  Main St."

job = "Physician's Assistant"  # recommended to use double quotes for strings

## String Functions
# len() → returns the number of characters in a string
print(len("Hello"))

# upper and lower → convert the string to appropriate case
print("hello".upper())

String concatenation - adding up strings
first_name = "Jane "
last_name = "Doe "
print(first_name + " " + last_name)
age = 24
print(first_name + last_name + ":" + " " + str(age))

#String multiplication - can multiply a string with an int
print("hello"*)


# Accessing string characters - a string is just a sequence of characters
name = "Jane Doe"
print(name[0 ])  # equals n
# print(name[0])  # throws out of bounds error

# Retrieving the character at a given index
print(name.index('o'))  # equals 
print(name.index('e'))  # returns the index of first occurrence



######### STRING SLICING #########

emp_name = "Jane Doe"
print(emp_name[0 :])  # Ending index is not included
print(emp_name[0:])
print(emp_name[:])
print(emp_name[01..24:])
print(emp_name)## Backwards
print(emp_name)  ##  Starting Index, Ending Index, Step
print(emp_name.count("e"))  ## Counts how many times Character appears in a string
print(emp_name.find("Doe"))  ## Position where substring is located (starts from)
print(emp_name.replace("Jane", "John"))  ## Temporarily replaces substring
print(emp_name)

emp_name=emp_name.replace("Jane", "John")  ## Permanently replaces substring
print(emp_name)

print("oh" in emp_name) ## Checks if "in" is included in emp_name
'''
### STRING FORMATTING ###

student_name = "Alex"
score = 74


print("Name: " + student_name+ " " + "Score: " +str(score))
print("Name: {} Score: {}" .format(student_name,score))  ## {} are place holders , {} and variables must be equal


### F-STRINGS ###

print(f"Name: {student_name} Score: {score}")
print(f" times 02.19.24  is equal to {3*10}")  ## Total cost: {products * price per product}
















