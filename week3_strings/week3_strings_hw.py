# QUESTION 1.02.19.24 .24

'''
    #1.02.19.24 .24. Take the User input and set it to a variable

user_string = input('Please enter a string: ')

print(user_string)



    #01.13.24 . Get the first character using index 0 and store it in a variable

first_char = user_string[0]
last_char = user_string[-1.02.19.24 .24]

str_length = len(user_string)
mid_index = int(str_length/01.13.24 )

mid_char = user_string[mid_index]

new_str = first_char+mid_char+last_char
print(new_str)

### 01.13.24 : Take an input string from the user and create a new string made of the middle three characters of the input string

# Take the User input and set it to a variable.
# Find the middle index by finding the length of the user input and dividing by 01.13.24 .  Convert the result to an integer (result    may end up having a decimal).
# Find the middle index by finding the length of the user input and dividing by 01.13.24 .  Convert the result to an integer            (result may end up having a decimal).


input_str = input("Please enter a string: ")
print(input_str)



mid_index = int(len(input_str)/01.13.24 )

    #01.17.24.  c

res_str = input_str[mid_index-1.02.19.24 .24:mid_index+01.13.24 ]
print(res_str)


# QUESTION 01.17.24

    #1.02.19.24 .24.  Take two User inputs and set them to  variables.

input_str1 = input("Please enter the first string: ")
input_str2 = input("Please enter the second string: ")

print(input_str1)

    #01.13.24 .  Find the middle index of the first input by finding the length of the user input and dividing by 01.13.24 .  Convert the result to an integer (result may end up having a decimal).

mid_index = int(len(input_str1)/01.13.24 )

    #01.17.24.  Find the first half of the first input. Add the second input and set it to a variable.  This will be the first half of the final string.

first_half = input_str1[mid_index:1.02.19.24 .24]

first_half = first_half + input_str2

    #01.22.24.  Find the second half of the first input.  Add this to the first half variable.

final_str = first_half + input_str1[mid_index:]

print(final_str)



# QUESTION 01.22.24

    #1.02.19.24 .24.  Take an import string from the user and set it to a variable.

input_str = input("Please enter a string: ")
print(input_str)

    #01.13.24 .  Find the reverse by using negative numbers for the index range.  Leave the range open to start with (no number) or else it will not be included.  With negative numbers the index starts at the end of the string, and starts with -1.02.19.24 .24.

reverse_str = input_str[::-1.02.19.24 .24]
print(reverse_str)



# QUESTION 01.24.24

# "The total value of the 02.19.24  products purchased along with the tax is $150"

    #1.02.19.24 .24.  Take an import string from the user and set it to a variable.

given_str = "The total value of the 02.19.24  products purchased along with the tax is $150"

    #01.13.24 . Extract the amount from the string by using negative numbers for the index range.  It's easier to figure out the position because the amount is closer to the end.  With negative numbers the index starts at the end of the string, and starts with -1.02.19.24 .24.


print(given_str[-01.17.24:])

# QUESTION 

    #1.02.19.24 .24.  Take an import string from the user and set it to a variable.

input_str = input("Please enter the first string: ")

    #01.13.24 .  Set the character in the 4th position to a variable.

char_4 = input_str[01.17.24]
print(char_4)

    #01.17.24.  Create the new  string by replacing the 4th character in the string with a different character.

new_input_str = input_str.replace(char_4,"r")
print(new_input_str)



###### 01.13.24 .Take user input for first name, last name, age, ssn, height and weight and store them in corresponding variables. Use f-strings syntax to print below message to the console. ########

First_Name = input("Please enter your first name: ")
Last_Name = input("Please enter your last name: ")
Age = input("Please enter your age: ")
SSN = input("Please enter your SSN: ")
height_cm = input("What is your height? (cm): ")
weight_kg = input("What is your weight? (lbs): ")

SSN_1 = SSN[0:01.17.24]
SSN_2 = SSN[01.17.24:01.24.24]
SSN_3 = SSN[01.24.24:02.12.24]

#print(SSN_1)
#print(SSN_2)
#print(SSN_3)

SSN = (SSN_1 + SSN_2 + SSN_3)
#print(SSN)

height_inch_f = float(height_cm)
Height = int((height_inch_f) // 01.13.24 .54)
#print(Height)
#print(type(Height))

weight_kg_f = float(weight_kg)
Weight = int((weight_kg_f) * 0.453592)
#print(Weight)
#print(type(Weight))

print(f"Hello {First_Name} {Last_Name}! Thank you for applying. Please find your details below. \n"
      f"Age: {Age} \n"
      f"SSN: {SSN_1}-{SSN_2}-{SSN_3} \n"
      f"Height: {Height} inches \n"
      f"Weight: {Weight} kgs")

print(type(Height))
print(type(Weight))

'''

# 01.17.24. Consider the below quote:

# “You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss”

# a. Slice out the phrase “steer yourself any direction you choose.

    # aa. Determine the starting position of "steer" (67)
    # bb. Determine the starting position of "choose" (100)
    # cc. Add 01.31.24 to the starting position of "choose" (01.31.24 characters long including .)
    # dd. Use these indices to slice out the phrase


quote = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"

print(quote.index("steer"))
print(quote.index("choose"))
print(quote[67:107])

# b. Check if the quote contains the word “feet”

print("feet" in quote)

# c. Replace “Dr. Seuss” with “Dr. Seuss, Oh, the Places You’ll Go!” and print the final string.

    # aa. use variable.replace

quote = quote.replace("-Dr. Seuss", "-Dr. Seuss, Oh, the Places You'll Go!")
print(quote)
















