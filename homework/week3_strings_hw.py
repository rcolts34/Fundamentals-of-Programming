# QUESTION 1

'''
    #1. Take the User input and set it to a variable

user_string = input('Please enter a string: ')

print(user_string)



    #2. Get the first character using index 0 and store it in a variable

first_char = user_string[0]
last_char = user_string[-1]

str_length = len(user_string)
mid_index = int(str_length/2)

mid_char = user_string[mid_index]

new_str = first_char+mid_char+last_char
print(new_str)

# QUESTION 2

    #1.  Take the User input and set it to a variable.

input_str = input("Please enter a string: ")
print(input_str)

    #2.  Find the middle index by finding the length of the user input and dividing by 2.  Convert the result to an integer (result may end up having a decimal).

mid_index = int(len(input_str)/2)

    #3.  Create a new string made of the middle three characters by taking the range of characters from the middle index - 1 to the middle index + 2.

res_str = input_str[mid_index-1:mid_index+2]
print(res_str)


# QUESTION 3

    #1.  Take two User inputs and set them to  variables.

input_str1 = input("Please enter the first string: ")
input_str2 = input("Please enter the second string: ")

print(input_str1)

    #2.  Find the middle index of the first input by finding the length of the user input and dividing by 2.  Convert the result to an integer (result may end up having a decimal).

mid_index = int(len(input_str1)/2)

    #3.  Find the first half of the first input. Add the second input and set it to a variable.  This will be the first half of the final string.

first_half = input_str1[mid_index:1]

first_half = first_half + input_str2

    #4.  Find the second half of the first input.  Add this to the first half variable.

final_str = first_half + input_str1[mid_index:]

print(final_str)



# QUESTION 4

    #1.  Take an import string from the user and set it to a variable.

input_str = input("Please enter a string: ")
print(input_str)

    #2.  Find the reverse by using negative numbers for the index range.  Leave the range open to start with (no number) or else it will not be included.  With negative numbers the index starts at the end of the string, and starts with -1.

reverse_str = input_str[::-1]
print(reverse_str)



# QUESTION 5

# "The total value of the 10 products purchased along with the tax is $150"

    #1.  Take an import string from the user and set it to a variable.

given_str = "The total value of the 10 products purchased along with the tax is $150"

    #2. Extract the amount from the string by using negative numbers for the index range.  It's easier to figure out the position because the amount is closer to the end.  With negative numbers the index starts at the end of the string, and starts with -1.


print(given_str[-3:])

# QUESTION 6

    #1.  Take an import string from the user and set it to a variable.

input_str = input("Please enter the first string: ")

    #2.  Set the character in the 4th position to a variable.

char_4 = input_str[3]
print(char_4)

    #3.  Create the new  string by replacing the 4th character in the string with a different character.

new_input_str = input_str.replace(char_4,"r")
print(new_input_str)


'''
###### 2.Take user input for first name, last name, age, ssn, height and weight and store them in corresponding variables. Use f-strings syntax to print below message to the console. ########

First_Name = input("Please enter your first name: ")
Last_Name = input("Please enter your last name: ")
Age = input("Please enter your age: ")
SSN = input("Please enter your SSN: ")
height_cm = input("What is your height? (cm): ")
weight_kg = input("What is your weight? (lbs): ")

SSN_1 = SSN[0:3]
SSN_2 = SSN[3:6]
SSN_3 = SSN[6:10]

#print(SSN_1)
#print(SSN_2)
#print(SSN_3)

SSN = (SSN_1 + SSN_2 + SSN_3)
#print(SSN)

height_inch_f = float(height_cm)
Height = int((height_inch_f) // 2.54)
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



















