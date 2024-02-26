'''

Functions - reusable blocks of code

# Write a function to check whether a number is even or not

'''

# num →  function parameter
# function definition ↓
def checkEven(num):
    result = ""
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

### Making a function call
print(checkEven(4))  # 4  →  function arguments
print(checkEven(9))

is_even = checkEven(311658115319861619689)
print(is_even)

# def print("Hello")   # does not have any return type
# import random
# randNum = random.random()    # returns a number


# Palindrome → write a program to check where a word is a palendrome
#             → takes one string
    # Ex : level , racecar, eye, mom
# Anagrams → write a program to chck where a word is a anagram
#          → takes two parameters
    # Ex : life / file ,




