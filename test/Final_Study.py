

'''

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q1: What will the output of the following Python code be?

for i in range(5):
    if i == 3:
        break
    print(i)

    ## A: A) 0 1 2 3

    ### Correction Answer: B) 0 1 2
        The break statement exits the loop when i becomes 3, so it stops before printing 3.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q2: Which collection type is best suited for accessing elements by a unique key?

A) List
B) Tuple
C) Set
D) Dictionary

    ## A: B) Tuple

    ### Correction Answer: D) Dictionary
        Dictionaries are ideal for key-value pair access, making them the best choice for accessing elements by a unique key.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q3: What is the correct way to handle multiple exceptions in Python?

try:
    # code that might throw an exception
except TypeError:
    # handle specific exception
except ValueError:
    # handle specific exception

    ## A: D) except TypeError and ValueError

     ### Correction Answer: C) except (TypeError, ValueError)

    The correct syntax to handle multiple exceptions in a single block is to enclose them in parentheses.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q4: What is the difference between parameters and arguments in functions?

A) Parameters are values, and arguments are variables.
B) Parameters define the variables, and arguments are the actual values provided.
C) Parameters are used in lambda functions only, while arguments are used in regular functions.
D) No difference, both terms mean the same.

    ## A: B)

    Parameters are the names used in the function definition, and arguments are the actual values passed to the function.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q5: What does the following Python expression represent?
(lambda x: x + 1)(5)

    ## A: C)

    This is an example of an IIFE where the lambda function is defined and immediately called with the argument 5.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q6: Which of the following is true about memoization and tabulation in dynamic programming?

A) Memoization is a top-down approach, while tabulation is bottom-up.
B) Memoization uses more memory than tabulation.
C) Tabulation can be applied to problems that memoization cannot solve.
D) Memoization is typically faster than tabulation.

    ## A: A

    Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again, and it is a top-down approach. Tabulation is the opposite, being a bottom-up approach.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Q7:  Which of the following is correct for reading a text file using the with statement in Python?

A) with open('file.txt', 'r') as file: print(file.read())
B) file = open('file.txt', 'r') with file: print(file.read())
C) with open('file.txt', 'r') print(file.read())
D) open('file.txt', 'r') as file: with print(file.read())

    ## A: A)

    This is the correct syntax to import a specific function from a module and alias it.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q8:






    ## A:

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q9: What will be the output of the following code snippet?

for i in range(5):
    if i == 3:
        continue
    print(i)

    ## A: B) 0 1 2 3 4

    ## Correct Answer: A) 0 1 2 4

         The continue statement skips the current iteration when i is equal to 3, so 3 is not printed.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q10: In Python, which collection type does NOT allow duplicate elements?

A) List
B) Tuple
C) Set
D) Dictionary

    ## A: B) Tuple

    ## Correct Answer: C) Set

        Sets in Python are designed to hold only unique elements, meaning no duplicates are allowed.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q11: What will the following code output if a KeyError occurs?

try:
    raise KeyError
except KeyError:
    print("Caught a key error!")
finally:
    print("Finally block executed.")

    ## A: C) Caught a key error! Finally block executed.

        The code catches the KeyError, prints a message, and the finally block executes regardless of the exception, printing its message.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q12: Which statement about lambda functions is true?

A) Lambda functions can only have one parameter.
B) Lambda functions cannot return values.
C) Lambda functions are just syntactic sugar for simple functions that return an expression.
D) Lambda functions can contain multiple statements.

    ## A: B) Lambda functions cannot return values.

        ## Correct Answer: C)  Lambda functions are just syntactic sugar for simple functions that return an expression.

        Lambda functions can indeed return values and are used for creating small anonymous functions that return a value.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q13: Which statement is true regarding recursion in Python?

A) Recursion in Python can handle very deep recursion depths without any issues.
B) Every recursive function can be transformed into a function that uses memoization.
C) Python automatically applies memoization to recursive functions to prevent stack overflow.
D) Recursion can lead to stack overflow if not handled properly or if the recursion depth is too deep.

    ## A: D) Recursion can lead to stack overflow if not handled properly or if the recursion depth is too deep.

        Python has a limit on the recursion depth (typically around 1000 nested calls), and exceeding this limit results in a stack overflow error.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q14: Which line of code correctly imports the json module and uses an alias?

A) import json as js
B) import json.json as js
C) from json import json as js
D) import 'json' as js

    ## A: A) import json as js

    This line correctly imports the json module with the alias js, which can then be used to refer to the module.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Q15: How would you open a CSV file in Python and read its rows as dictionaries?

A) Use the csv.reader method from the csv module.
B) Use the csv.DictReader method from the csv module.
C) Open the file normally and manually convert each line to a dictionary.
D) Use the read_csv method from the csv module.

    ## A: B) Use the csv.DictReader method from the csv module.

    csv.DictReader reads each row of the CSV file as a dictionary, where the keys correspond to the field names specified in the header.

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

'''