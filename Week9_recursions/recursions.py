## Recursion
# A process in which a function repeatedly calls itself as long a condition is satisfied.
# an extension of loops
# Recursion calls are not recommended if there are an excessive amount of recursion calls to be made
# Whenever you call a function (b) within a function (a), the initial function will pause (a) until (b) has finished executing.

'''

def sayHello(name):
    print(f"Hello {name}!")

def userDetails():
    user_name = input("Enter a name: ")
    sayHello(user_name)
    user_city = input("Enter a city: ")
    print(f"You are from {user_city}")
userDetails()

#### RECURSION FUNCTION

# test1
# printing the value
# "3"
# calling the function
# printing the value
# "2"
# calling the function

def test1(n):
    if(n > 0):
        print("Printing the value. ")
        print(n)
        print("Calling the function")
        test1(n - 1)
test1(3)


### test2
# Print "n" is paused until the function has stopped running
# Once the function has stopped running, control is given back to the parent function (Parent → Child , test2(3) → test2(2), etc
# Temporary values are stored in "stack memory" with time stamps

def test2(n):
    if(n > 0):
        print("Calling the function")
        test2(n - 1)
        print("Printing the value. ")
        print(n)
test2(3)


### Find the factorial of a number

#             - n!              = n x (n-1)!
# factorial   - 5! - 5x4x3x2x1  = 5 x 4!
#             - 4! - 4x3x2x1    = 4 x 3!
#             - 3! - 3x2x1      = 3 x 2!
#             - 2! - 2x1        = 2 x 1!
#             - 1!              = 1 x 0!
#             - 0!              = 1

# Write a function to find the factorial of a number

# 5 x 4 !

'''

# 1000! → 1000 x 999! →  999! x 998! → .......!0
# if you are making that many recursive calls, it is not the place to use recursion

# def findFactorial(num):
#     if (num < 0):
#         print("Please provide a positive number: ")
#         return
#     elif (num <= 1):
#         return 1
#     else:
#         return num * findFactorial(num-1)
# factorial_value = findFactorial(1000)
# print(factorial_value)



### Fibonacci Series
# Every number is the sum of the previous two numbers (starting from third number)
# Try to write recursive program that prints Fibonacci Series

# Fibonacciseries(5)
# Prints → 11235
# Fibonacciseries(6)
# Prints → 112358
# Fibonacci →

# Reuse the code provided, add explaination
# Create quicksort.py file
# Add quicksort.py and recursion.py to archive and upload for Homework
# Due on Friday
# Classes may be online, watch email

def fibSeries(n):
     list1 = []
     for i in range(n):
         if i > 0:
             list1.append(i)
             list1_sum = sum(list1)













# Quick sort
#     1. Fine the median value
#     2. Create 3 lists
#         a. First list → has all the values < median value
#             →  median([list1[0], list1[len(list1)/2], list1[[-1]]])
#             →  median([31, 92, 28]) = 31
#         b. Second list → has all the values = median value
#        ||     < 31 →  [18, 18, 3, 11, 28]   |  = 31  → [31]     |  > 31  →  [72, 79, 92, 44, 56, 41]  ||
#         c. Third list → has all the values > median value
#             →  median(18, 3, 28) = 18
#        ||     < 18 →  [3, 11]               |  = 18 → [18, 18]  |  > 18  →  [28]                      ||
#             →  median(3, 11, 11) = 11
#        ||     < 11 → [3]                    |
#     3. Repeat step 1 and step 2 for first and third lists until there is only one element left in each list
#                         [72, 79, 92, 44, 56, 41]
#             →  median([72, 44, 41]) = 44
#        ||     < 44 → [41]                   | → = 44 [44]       |  > 44  → [72]





#### Quick Sort

    # 1. Find the median value
    # 2. Create 3 lists
    #     a. First list → has all the values < median value
    #     b. Second list → has all the values = median value
    #     c. Third list → has all the values > median value
    # 3. Repeat step 1 and step 2 for first and third lists until there is only one element left in each list

num_list = [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]

import statistics
def quickSort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        median_value = statistics.median([num_list[0], num_list[len(num_list)//2], num_list[-1]])
        left_list = []
        middle_list = []
        right_list = []
    for i in num_list:
        if i < median_value:
            left_list.append(i)
        elif i > median_value:
            right_list.append(i)
        else:
            middle_list.append(i)
    return(quickSort(left_list) + middle_list + quickSort(right_list))

sorted_list = quickSort(num_list)
print(sorted_list)

# sorted_list = quickSort([31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28])
# print(sorted_list)


