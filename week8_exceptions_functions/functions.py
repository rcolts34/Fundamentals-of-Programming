'''

Functions - reusable blocks of code

# Write a function to check whether a number is even or not

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

'''

# For Homework
# Palindrome → write a program to check whether a word is a palindrome
#             → takes one string
    # Ex : level , racecar, eye, mom
# Anagrams → write a program to chck whether a word is an anagram
#          → takes two parameters
    # Ex : life / file ,


### Write a program to check whether a word is a palindrome


def checkPal(string):
    result = ""
    if string[0::] == string[::-1]:
        result = True
    else:
        result = False
    return result

print(checkPal("racecar"))
print(checkPal("rotator"))
print(checkPal("deified"))
print(checkPal("racecar"))
print(checkPal("racecar"))
print(" Go hang a salami, Im a lasagna hog.")
print(checkPal("gohangasalamiimalasagnahog"))
print("Now saw ye no mosses or foam, or aroma of roses. So money was won.")
print(checkPal("nowsawyenomossesorfoamoraromaofrosessomoneywaswon"))
print(checkPal("thisisnotapalindrome"))






