

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



# For Homework
# Palindrome → write a program to check whether a word is a palindrome
#             → takes one string
    # Ex : level , racecar, eye, mom
# Anagrams → write a program to chck whether a word is an anagram
#          → takes two parameters
    # Ex : life / file ,

'''

### 1. Write a program to check whether a word is a palindrome

def is_pal(word):
    result = ""
    if word == word[::-1]:
        result = True
    else:
        result = False
    return result

result = is_pal()
print(result)

print(is_pal("racecar"))
print(is_pal("rotator"))
print(is_pal("deified"))
print(is_pal("racecar"))
print(is_pal("racecar"))
print(" Go hang a salami, Im a lasagna hog.")
print(is_pal("gohangasalamiimalasagnahog"))
print("Now saw ye no mosses or foam, or aroma of roses. So money was won.")
print(is_pal("nowsawyenomossesorfoamoraromaofrosessomoneywaswon"))
print(is_pal("thisisnotapalindrome"))

### Write a program to check whether two words are anagrams

# def checkAna(word):
#     result = ""
#     if string[0::] == string[::-1]:
#         result = True
#     else:
#         result = False
#     return result

# worda = listen
# wordb = silent


def is_anagram(str1, str2):
    result = ""
    str1 = ""
    str2 = ""
    list1 = ""
    list2 = ""
    for char in str1:
        list1.append(char)
    list1 = sorted(str1)
    for char in str2:
        list2.append(char)
    list2 = sorted(str2)
    if list1 == list2:
        result = True
    else:
        result = False
    return result

result = is_anagram("astronomer", "moonstarer")
print(result)

print(is_anagram("astronomer", "moonstarer"))


# def is_anagram(str1, str2):
#     str1_sorted = str(sorted(str1))
#     print(str1_sorted)
#     str2_sorted = str(sorted(str2))
#     if (str1_sorted == str2_sorted):
#         return "Anagrams"
#     else:
#         return "Not Anagrams"
# 
# 
# result = is_anagram("life", "file")
# print(result)
# 
# print(is_anagram("listen", "silent"))


'''

### 3. Write a function to that takes user name, birth year, budget, price of the product as inputs and performs the following operations.

# a. Calculates the current age based on the birth year
# b. Calculates the number of products that can be bought based on budget and price per product. Round down the number of products.
# c. Displays the message as shown in sample output
# d. Identify the potential exceptions and structure your code using try, except(s), else, and finally blocks

## Try except , else, finally
## take inputs, see what errors might occur
##

def user_info("str1", int1, int2, int3):
    print(input("Enter your name: "))
    print(int(input("Enter your birth year: ")))
    print(int(input("Enter your budget: ")))
    print(int(input("Enter the price of the product: ")))
    current_age = 2024 - int1
    amount = int2 / int3


print(user_info("bob", 1988, 5000, 45))
# result = user_info("bob", 1988, 5000, 45)
# print(result)

print(user_info(result))
print(user_info(str1, int1, int2, int3))



str1 = input("Enter your name: ")
int1 = int(input("Enter your birth year: "))
int2 = int(input("Enter your budget: "))
int3 = int(input("Enter the price of the product: "))


















