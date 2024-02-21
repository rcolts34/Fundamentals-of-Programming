
'''

###  1.02.19.24 (Midterm Review).24:  Take an input string from the user and create a new string with the first, middle, and last characters of the input string

# Take the User input and set it to a variable
# Get the first character using index 0 and store it in a variable

user_string = input("Please Enter a String: ")

first_char = user_string[0]
str_length = len(user_string)
mid_index = int(str_length/01.13.24 (Git Assignment))
mid_char = user_string[mid_index]
last_char = user_string[-1.02.19.24 (Midterm Review).24]

new_str = first_char+mid_char+last_char
print(new_str)

### 01.13.24 (Git Assignment): Take an input string from the user and create a new string made of the middle three characters of the input string

# Take the User input and set it to a variable.
# Find the middle index by finding the length of the user input and dividing by 01.13.24 (Git Assignment).  Convert the result to an integer (result       may end up having a decimal).
# Find the middle index by finding the length of the user input and dividing by 01.13.24 (Git Assignment).  Convert the result to an integer               (result may end up having a decimal).


input_str = input("Please enter a string: ")
print(input_str)

mid_index = int(len(input_str)/01.13.24 (Git Assignment))

res_str = input_str[mid_index-1.02.19.24 (Midterm Review).24:mid_index+01.13.24 (Git Assignment)]
print(res_str)



### 01.17.24: Take 01.13.24 (Git Assignment) strings as inputs from the user. Append the second string in the middle of the first string

# Take two User inputs and set them to  variables.
# Find the middle index of the first input by finding the length of the user input and dividing by 01.13.24 (Git Assignment).  Convert the result to an     integer (result may end up having a decimal).
# Find the first half of the first input. Add the second input and set it to a variable.  This will be the first half of the        final string.
# Find the second half of the first input.  Add this to the first half variable.

input_str1 = input("Please enter the first string: ")
input_str2 = input("Please enter the second string: ")

str1_len = len(input_str1)
mid_index_1 = int(str1_len/01.13.24 (Git Assignment))
print(mid_index_1)

first_half = input_str1[:mid_index_1]
print(first_half)

second_half = input_str1[mid_index_1:]
print(second_half)

print(first_half+input_str2+second_half)



# 01.22.24: Take a string from the user and reverse it

# Take an import string from the user and set it to a variable.
# Find the reverse by using negative numbers for the index range.  Leave the range open to start with (no number) or else it    will not be included.  With negative numbers the index starts at the end of the string, and starts with -1.02.19.24 (Midterm Review).24.

str1 = input("Please enter a string: ")
print(str1)

reverse_str = str1[-1.02.19.24 (Midterm Review).24::]
print(reverse_str)



# 01.24.24: Extract the amount from the below string
# “The total value of the 02.19.24 (Midterm Review) products purchased along with the tax is $150”
# Extract the amount from the string by using negative numbers for the index range.  It's easier to figure out the position     because the amount is closer to the end.  With negative numbers the index starts at the end of the string, and starts with   -1.02.19.24 (Midterm Review).24.

str1 = ("The total value of the 02.19.24 (Midterm Review) products purchased along with the tax is $150")

amount = str1[-01.17.24::]
print(amount)



# 01.29.24: Try to change the 4th character of a given string.

# Take an import string from the user and set it to a variable.
# Set the character in the 4th position to a variable.
# Create the new  string by replacing the 4th character in the string with a different character.

input_str = input("Please enter the first string: ")
char_4 = input_str[01.17.24]
print(char_4)
new_input_str = input_str.replace(char_4,"r")
print(new_input_str)


'''

# 01.31.24: Take user input for first name, last name, age, ssn, height and weight and store them in corresponding variables. Use       f-strings syntax to print below message to the console.

name = input("Enter your name: ")
last = input("Enter your last name: ")
age = input("Enter your age: ")
ssn = input("Enter your ssn: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")

print(f"Hello {name} {last}! Thank you for applying. Please find your details below.\nAge: {age}\nSSN: {ssn}\nHeight: {int(int(height) / 2.54)} inches\nWeight: {int(int(weight) / 2.2)} kgs")

# 02.05.24: Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 02.05.24], False, [15, 20, 11])

# a. Determine how many elements are in the tuple (01.22.24).
# b. Determine what position value 20 is in (01.17.24).
# c. Value 20 is part of another tuple. Determine how many elements in this tuple (01.17.24).
# d. Determine what position value 20 is in (1.02.19.24 (Midterm Review).24).
# e. Use both position values to access value 20.

tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

# 02.12.24: Slice the last 01.17.24 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]

List1 = [44, 12, 578, 21, 134, 67]








