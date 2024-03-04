'''

# Functions - reusable blocks of code

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
# print(checkEven(4))  # 4  →  function arguments
# print(checkEven(9))
#
# is_even = checkEven(311658115319861619689)
# print(is_even)

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




### 3. Write a function to that takes user name, birth year, budget, price of the product as inputs and performs the following operations.

# a. Calculates the current age based on the birth year
# b. Calculates the number of products that can be bought based on budget and price per product. Round down the number of products.
# c. Displays the message as shown in sample output
# d. Identify the potential exceptions and structure your code using try, except(s), else, and finally blocks

## Try except , else, finally
## take inputs, see what errors might occur
##

def user_info(str1, int1, int2, int3):
    result = ""
    name = str1
    dob = int1
    budget = int2
    price = int3
    result = f"Hello {name}! You are {2024-dob} years old and you can buy {round(budget/price)} products"
    return result
    
user_info('steve', 1975, 400, 75)
print(result)

result = user_info('steve', 1975, 400, 75)
print(result)
print(user_info('steve', 1975, 400, 75))


'''

def user_info(name, dob, budget, price):
    result = ""
    name = input("Enter your name: ")
    dob = int(input("Enter your birth year: "))
    budget = int(input("Enter your budget: "))
    price = int(input("Enter the price of the product: "))
    result = f"Hello {name}! You are {2024-dob} years old and you can buy {round(budget/price)} products"


user_info("", "", "", "")
print(user_info)

### 4. Write a program to check whether we can create a triangle or not.

# Given three sticks, you may be able to arrange them into a triangle.  Ex: Sticks - 12" , 1", 1" - Cannot make a triangle.
# If any of the 3 lengths is > than the sum of the other 2, you cannot form a triangle. Otherwise, you can.
# If the sum of the two lengths equals the third, they from a "degenerate" triangle".
# Write a function named is_triangle that takes three int arguments, and prints yes or no depending on whether or not you can form a triangle with given lengths.

def is_triangle(length1, length2, length3):
    length1 = ""
    length2 = ""
    length3 = ""

























