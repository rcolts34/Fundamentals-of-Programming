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

    # Function is created that checks whether a word is a palindrome.  A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
    # If logic → if string passed to the function is the same forward as it is backwards, the result is true (is Palindrome).
        # The [::-1] reverses the string  → negative step instructs to start at the end of the string, and empty start and stop values ensure that the entire string is included regardless of length [start:stop:step]
    # Else logic → If any other result occurs other than string forward = string backwards (result = True), then result = false.  The only other possible outcome is string forward != string backwards.
    # result is returned
    # Function is called and a parameter (string) can be passed to the function to check whether it is a palindrome.
    # Result is printed.

def is_pal(word):
    result = ""
    if word == word[::-1]:
        result = True
    else:
        result = False
    return result

result = is_pal("deified")
print(result)

### 2. Write a program to check whether two words are anagrams

    # Function is created that checks whether two words are anagrams.  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    # Characters in both strings are sorted alphabetically, set to variables, and printed.
    # If logic → if the first 1st string (sorted alphabetically) = 2nd string (sorted alphabetically), the strings (words) are anagrams.
        # Since anagrams are created by taking a same word and rearranging the letters, words that are anagrams of each other must contain the same letters.  If the words are anagrams, and the characters are sorted alphabetically, then they will be identical.
    # Else logic → If any other result occurs other than string1(sorted) = string2(sorted), then the words are not anagrams.  The only other possible outcome is string1(sorted) != string2(sorted).
    # Function is called and two parameters (strings) can be passed to the function to check whether they are anagrams.
    # Result is printed.

def is_anagram(str1, str2):
    str1_sorted = str(sorted(str1))
    print(str1_sorted)
    str2_sorted = str(sorted(str2))
    print(str2_sorted)
    if (str1_sorted == str2_sorted):
        return "Anagrams"
    else:
        return "Not Anagrams"

print(is_anagram("astronomer", "moonstarer"))



### 3. Write a function to that takes user name, birth year, budget, price of the product as inputs and performs the following operations.

    # Function is created that takes user information and outputs a statement
    # User is asked for name, DOB, budget, and price of product.  These results are set to variables.  The latter three are converted to int type.
    # Result is defined as an f statement that greats the user, calculated age by subtracted DOB from current year, and calculates how many products can be bought by dividing budget by the price.  Number of products is rounded to zero decimal places
    # The result is returned.
    # The function is called.  The function asks for the inputs that the f string uses, so the function doesn't have required parameters.

# a. Calculates the current age based on the birth year
# b. Calculates the number of products that can be bought based on budget and price per product. Round down the number of products.
# c. Displays the message as shown in sample output
# d. Identify the potential exceptions and structure your code using try, except(s), else, and finally blocks

## Try except , else, finally
## take inputs, see what errors might occur



def user_info():
    try:
        result = ""
        name = input("Enter your name: ")
        dob = int(input("Enter your birth year: "))
        budget = int(input("Enter your budget: "))
        price = int(input("Enter the price of the product: "))
        result = f"Hello {name}! You are {2024-dob} years old and you can buy {round(budget/price)} products."
    except ValueError as e:
        print("Something went wrong -", e)
    except ZeroDivisionError as e:
        print("Something went wrong - ", e)
    except Exception as e:
        print("Something went wrong -", e)
    else:
        print("From else: ", result)
    finally:
        return result

print(user_info())

'''

### 4. Write a program to check whether we can create a triangle or not.

# Given three sticks, you may be able to arrange them into a triangle.  Ex: Sticks - 12" , 1", 1" - Cannot make a triangle.
# If any of the 3 lengths is > than the sum of the other 2, you cannot form a triangle. Otherwise, you can.
# If the sum of the two lengths equals the third, they from a "degenerate" triangle".
# Write a function named is_triangle that takes three int arguments, and prints yes or no depending on whether or not you can form a triangle with given lengths.

    # Function is created that takes 3 sticks and determines if a triangle can be created based on length. If any of the three lengths is greater than the sum of the other two, you cannot form a triangle

    # Sticks are put in a list and assigned to a variable
    # Sticks list is sorted from smallest to largest and assigned to a variable
    # If logic → If any of the three lengths is greater than the the sum of the other two, a triangle cannot be made.  The sticks have been sorted from smallest to largest, so using sum and slicing the list to select the first two positions will add up the shortest two sticks.  If this sum is larger than the longest stick, a triangle can be made.
    # Else logic → The only other possible outcome is that the longest stick is longer than the sum of the two smaller sticks.  In this case, no, a triangle cannot be made.
    # The function is called, and printed.  Parameters must be entered (sticks 1-3 length).


def is_triangle(stick1, stick2, stick3):
    sticks = [stick1, stick2, stick3]
    sticks_sorted = sorted(sticks)

    if sum(sticks_sorted[0:2]) >= sticks_sorted[2]:
        return "Yes"
    else:
        return "No"

print(is_triangle(7, 10, 5))
print(is_triangle(30, 20, 24))
print(is_triangle(1, 1, 3))
print(is_triangle(6, 3, 2))