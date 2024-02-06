# QUESITON 1:  Take an input string from the user and create a new string
 # with the first, middle, and last characters of the input string

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




