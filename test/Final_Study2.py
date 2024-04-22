
'''

#### Collections

Types
○ Lists
    §  # 1. Allow duplicate data
    §  # 2. Order is maintained
    §  # 3.  Allows heterogenous data
        □ Different data types
    §  # 4.  Allows indexing and slicing

    §  ### New elements can be added to a list using append, insert, or extend ###
        □ Append
            ® List.append("item")
            ®  # append always adds elements at the end of the list
        □ Insert
            ® List.insert(location, "item"
            ®  # insert and be used to add an element at a particular location
        □ Extend
            ®  # extend is an inplace function so it changes the object internally but does not return anything
        □ Sort


○ Tuples
    §  # 1.  Cannot be modified  i.e cannot update, add, or remove an element
        □ Good for restricting data
            Ex: only inches, cms
            Ex: Bank Accounts - only 2 allowed

○ Sets
    # 1.  Do not allow duplicates
    # 2. Order is not guaranteed
        Ex:
            □ CustomerSSN can only exist once
            □ Logindatabase - user email can only exist once
            □ Intersection

○ courses1 = {'English', 'Data Analytics', 'Economics', 'History'}
    § print(courses.union(courses1))
    § print(courses.intersection(courses1))

    § print(courses.difference(courses1))
    § print(courses1.difference(courses))

Dictionaries
    collection of key value pairs
        Ex:
          employee_dict = [
            {
                "id": 1234,
                "name": "John",
                "skills": ["Java", "PHP", "Python"],
                "address": {
                    "city": "LA",
                    "state": "CA",
                    "zip-code": 12344
                }
            }
            ,
            {
                "id": 1235,
                "name": "John",
                "skills": ["Java", "PHP", "Python"],
                "address": {
                    "city": "LA",
                    "state": "CA",
                    "zip-code": 12344
                }
            }
        ]

####### ACCESSING ELEMENTS FROM COLLECTIONS ######
• list1 = [32, 34, 5, [45, 364, 23], [34, 7, 10, [34, 657, 11]], 11]
    • print(list1[4][3][1])
    • # tuples also support indexing and slicing
• TypeError: 'set' object is not subscriptable
    ○ Not indexable
    ○ Sets do not maintain order
        § Position is not fixed
• Empty Collections
    ○ # list1 = []
        § bracket
    ○ # tuple1 = ()
        § parenthesis
    ○ # dict1 = {}
        § Flower bracket
    ○ # set1 = set()
        § Set parenthesis
    ○ # tuple1 = (10, )
        Single


- Which collection type is best suited for accessing elements by a unique key?

A) List
B) Tuple
C) Set
D) Dictionary

D) Dictionary

        Dictionaries are ideal for key-value pair access, making them the best choice for accessing elements by a unique key.

- Which collection type does NOT allow duplicate elements?

A) List
B) Tuple
C) Set
D) Dictionary

C) Set

    Sets in Python are designed to hold only unique elements, meaning no duplicates are allowed.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### Continue and Break

• Continue
    skips the next lines in the execution and repeats
• Break
    stops the loop

#### Break

for i in range(5):
    if i == 3:
        break
    print(i)

0 1 2

    The break statement exits the loop when i becomes 3, so it stops before printing 3.

#### Continue

for i in range(5):
    if i == 3:
        continue
    print(i)

0 1 2 4

    The continue statement skips the current iteration when i is equal to 3, so 3 is not printed.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### Exception / Error -- unwanted scenario that disrupts the normal flow of your program

# Unwanted Scenario
    Also known as compile time errors
        Syntax Errors
                Ex: Missing
        Specific to language
        Handled by the Dev

# Logical errors
    Also known as run time exceptions
    - Divide by zero
    - int(input('t'))
    - Language agnostic
    - Caught by IDE
    - Stack Trace
        Error printout in console

print(a/b) # syntactically correct but incorrect logic wise so the error would be thrown only when running the program

try:
    print(a/b)

except Exception:
    print('Something Went Wrong')

print('End')

try:
    print("connection opened")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    result = a / b
except ZeroDivisionError as e:
    print("something went wrong-  ", e)
except ValueError as e:
    print("something went wrong- ", e)
except Exception as e:
    print("something went wrong-", e)
else:
    print(result) # else block code would run only if there are no errors thrown form the try block
finally: # used for the code that needs to be executed no matter what
    print("connections closed")
print("End")


    # Critical statement
    # print(a/b) # syntactically correct but incorrect logic wise so the error would be thrown only when running the program

# range is for when you don't already have a list.

numbers = [1, 2, 3, 4, 0, 5, 6]

for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)

        result = 10/num
        print(result)

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### Functions

    ## General

# Parameters are the names used in the function definition, and arguments are the actual values passed to the function.
    # Ex:       Num  →  parameter               6  →  argument

        # def checkEven(num):
        #     result = ""
        #     if num % 2 == 0:
        #         result = True
        #     else:
        #         result = False
        #     return result
    #print(checkEven(6))

# Functions - reusable blocks of code

____________________________________________________________________________________________________________________

    ## Lambda Function

# Lamda Functions good for one or two operations, otherwise use regular function

    # Exs:

        square_num1 = lambda a: a * a
        print(square_num1(5))

        add_nums = lambda a, b: a + b
        print(add_nums(4,5))

        hello_user = lambda name: f"Hello {name}!"
        print(hello_user("Carl"))

# Immediately Invoked Function Expressions (IIFEs)

    # AKA Annoynymous Functions
    # Function is not stored anywhere.
    # Used only when you want to use it immediately and use it one time.

        Exs:
            print((lambda name: f"Hello {name}!")('Jane'))
            print((lambda x: x + 5)(10))

____________________________________________________________________________________________________________________

    ## Higher Order Functions

# Filter
    # Expects two parameters: function, data
    # Picking out items from a list based on certain conditions
    # filter(function, data)

        Exs:

        nums = [3, 2, 6, 8, 4, 6, 2, 9]
        def is_even(n):
            return n % 2 == 0
        even_nums = list(filter(is_even, nums))
        print(list(even_nums))

        even_nums1 = list(filter(lambda x:x % 2 == 0, nums))
        print(list(even_nums1))

# Map
    # Used to perform some operation on every element in a list

        Exs:

        def double_num(n):
            return n * 2
        doubles = map(double_num, nums)
        print(list(doubles))

        doubles1 = map(lambda x:x * 2, nums)
        print(list(doubles1))

        # Using map and lambda, return a list with the lengths of all the cities

        cities = ["New York", "Miami", "Phoenix", "Columbus", "Pittsburgh"]
        lengths = map(lambda x: len(x), cities)
        print(list(lengths))

# Reduce
    # Used to obtain a single value from a given list
        # Calculating one value from a given list
        # Example → Find the sum of all numbers in a list

        Exs:

        nums = [3, 2, 6, 8, 4, 6, 2, 9]

        from functools import reduce
            # a → accumulator
            # b → current value
        def add_all(a, b):
            return a + b
        total_sum = reduce(add_all, nums)
        print(total_sum)

        total_sum1 = reduce(lambda a,b: a+b, nums)
        print(total_sum1)

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### Dynamic Programming

∟ Recursion forms the basis for:
    - Memoization:
        > Storing the results of sub-problems and reusing them later
        > Uses recursion
        > Top Down approach
    - Tabulation
        > Most widely used Dynamic Programming technique
        > Iterative approach
        > Does not use recursion
        > Bottom Up approach

∟ Need to understand the pattern to implement Memoization or Tabulation
    - Recursion  →  to understand pattern
          ↓
    - Memoization
          ↓
    - Tabulation  →  ideal approach

∟ Steps in Dynamic Programming

    1. Break down the complex problem into simpler sub-problems
    2. Find optimal solution to these sub-problems
    3. Store results / solutions of sub-problems (Memoization)
    4. Reuse the results / solutions of sub-problems so that a given sub-problem is not calculated more than once
    5. Calculate the result of the complex problem by combining the solutions of sub-problems
        > Applicable to problems which have:
            - Overlapping sub-problems (possibility of having duplicate calculations)
            - Final solution can be obtained by combining optimal solutions of sub-problems
                → A.K.A - Optimal Sub-structures

∟ Dynamic Programming is well suited for optimization problems
    - Finding best solutions that take minimum possible time
    - Use minimum possible memory
        > Ex: Transportation  →  shortest path
    - Recursion  →  Memoization  →  Tabulation
        2^n             n               1

∟ Time Complexity:
    - Number of opens (calls) that are required to solve the problem
    - As the number of operations increases, time complexity increases
        Ex: Quicksort  →  O(n^2)

∟ Space Complexity:
    - Memory usage

∟ It is desired that both Time Complexity and Space Complexity values are low.

∟ Undesirable:   Try to avoid
    - o(n!)
    - o(2n)         →   (Recursion)
    - o(n^2)
∟ Desirable:
    - o(n log n)    →                       Linear Relation
    - o(n)          →   (Memoization)   →   Attempting to determine 5th number in Fibonacci series, takes 5 calls
    - o(log n)
    - o(1)          →   (Tabulation)    →   Constant time or space complexity → Irrespective of n value, only need 1 function call.

 │════│════│════│════│═══│════│════│════│════│
 │    │ A  │ A  │ A  │ A │ A  │ A  │ A  │ A  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│
 │ A  │ 0  │ 0  │ 0  │ 0 │ 0  │ 0  │ 0  │ 0  │
 │════│════│════│════│═══│════│════│════│════│













═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### Modules

 1.  Standard
        -  Built into the language itself
            → EX:  import random

    2.  External
        - Not part of the language itself
        - Have to install them before importing
            → EX:  pandas, numpy
                ∟ Most widely used in data science and machine  learning
        - Pandas is always aliased as 'pd'
            → import pandas as pd
        - You can specifically import functions from an external library
            ∟ Library may be very large, don't want to import things you don't need
            ∟ from find_index_module import find_index
        - Running export modules in the background can use resources.  Don't want to have them running if you dont need them. Adding print statements can inform that they are running.
            ∟ print('Running find index module: ', __name__)
        - Add if condition to stop module from running
            ∟ when file is run directly
            ∟ if __name__ == '__main__':
                ∟ stops imported code from running in the background
    3.  Custom
        - Built by developers for their specific use cases
        - Exists in a separate file, and is called, similar to a function

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#### File Handling

    ### File Handling Read

1. Using the open command with files
      →  read  - display file, cannot overwrite
      →  write - create a new file and include some new data
      →  append - add to already existing content
    default mode is read
    once you open a file you must excplicitly close it

file_obj = open('sample_text', 'r')
print(file_obj.name)
print(file_obj.mode)
file_obj.close()

with open('sample_text', 'r') as file_obj:
    # print(file_obj.name)
    # # print('Inside with the open: ', file_obj.closed)
    # file_contents = file_obj.read()
    # print(file_contents)


    # To access one line at a time
    # for line in file_obj:
    #     print(line)

    # file_content = file_obj.readline()
    # print(file_content)

    # file_content = file_obj.readline()
    # print(file_content)

    # file_content = file_obj.readline()
    # print(file_content)

    size_to_read = 100

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # file_contents = file_obj.read(size_to_read)
    # print(file_contents)

    # When there are no more characters to return, read will return an empty string

    file_contents = file_obj.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = file_obj.read(size_to_read)

    file_obj.write('Writing')

# print(file_obj.closed)

    ### File Handling Write

# with open('write_test.text', 'w') as file_obj:
#     file_obj.write('Writing')

with open('sample_text', 'r') as read_obj:
    with open('sample_text_copy', 'w') as write_obj:
        write_obj.write('\n' + 'Rewriting again and again')
        # for line in read_obj:
        #     write_obj.write(line)

# csv, excel  →  pandas

    ### JSON intro

### JSON  →  Java script object notation

 emp_data = '''
# {
#     "employees": [
#         {
#             "name": "John",
#             "age" : 29,
#             "emails": ["john@gmail.com", "john@outlook.com"]
#         },
#         {
#             "name": "Jane",
#             "age" : 48,
#             "emails": null
#         }
#     ]
# }
# '''

# To load JSON string into a python object (convert json string into python object)

# import json
# json_data = json.loads(emp_data)
# print(json_data)
# print(type(json_data))
# print(json_data["employees"])

# # for emp in json_data["employees"]:
# #     print(emp["name"])

# # Delete the email for each employee and then load it into a json string (python object  →  json string)
# for emp in json_data["employees"]:
#     del emp["emails"]
#     pass

# # print(json_data)

# # Convert a python object into a json string
# # indent  →  makes output easier to read

# new_string = json.dumps(json_data, indent=2)
# print(new_string)
# print(type(new_string))


#═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

    ###   API  →  Application Programming Interface

#____________________________________________________________________________________________________________________
# Address  →  user entered address 16701 , recommended address: 16701-1234
# web application  →  USPS Public API (API call) →  validate and return appropriate address
#____________________________________________________________________________________________________________________

#____________________________________________________________________________________________________________________
# Fidelity Investments  →  facebook page, twitter handle, linked in (API call for data related to Fidelity)
# Facebook API  →  JSON format
# posts, comments, replies, etc...
#____________________________________________________________________________________________________________________

# import random

#   random[package].random()[function]
#   ctrl + click  →  takes you to source code of package or library

# random.random()

#   Load JSON data from a file into python object

# import json
#
# with open('states.json', 'r') as file_obj:
#   data = json.load(file_obj)

#   print(data)
#   print(type(data))

# for state in data['states']:
#   print(state['name'], state['abbreviation'])

#   remove the area code for each state
#     del state['area_codes']

# print(data['states'])

#   To write json data to a file

# with open('new_states.json', 'w') as file_obj:
#   json.dump(data, file_obj, indent=2)

# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

'''